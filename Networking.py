import socket
import argparse
import time
import os
import binascii
import json
import traceback
from Cryptography.nacl import NaCl
from threading import Thread, Lock
from Packets.Factory import *
from Logic.Device import Device
from Packets.Messages.Server.LobbyInfoMessage import LobbyInfoMessage
from Packets.Messages.Server.TeamErrorMessage import TeamErrorMessage
from Logic.Player import Player

connected_clients_count = 0
client_count_lock = Lock()

class Networking(Thread):
    Clients = {"ClientCounts": 0, "Clients": {}}
    def __init__(self):
        Thread.__init__(self)

        self.settings = json.load(open('Settings.json'))
        self.usedCryptography = self.settings["usedCryptography"]
        self.address = self.settings["Address"]
        self.port = self.settings["Port"]
        self.server = socket.socket()
        self.nacl = NaCl()
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):

        global connected_clients_count
        self.server.bind((self.address, self.port))
        
        print('Server is listening on {}:{}'.format(self.address, self.port))
        #self.server.bind(("192.168.1.184", 5555))
        while True:
            self.server.listen(5)
            client, address = self.server.accept()
            global connected_clients_count
            with client_count_lock:
                connected_clients_count += 1
                print(f"Connected clients: {connected_clients_count}")
            
            print('New connection from {}'.format(address[0]))
            clientThread = ClientThread(client, address).start()


class ClientThread(Thread):
    def __init__(self, client, address):
        Thread.__init__(self)
        self.address = address
        self.client = client
        self.device = Device(self.client)
        self.player = Player(self.device)
        self.settings = json.load(open('Settings.json'))
        self.usedCryptography = self.settings["usedCryptography"]
        self.debug  = True

    def recvall(self, size):
        data = b''
        while size > 0:
            s = self.client.recv(size)
            if not s:
                raise EOFError
                break
            data += s
            size -= len(s)
        return data

    def run(self):

        global connected_clients_count

        try:
            while True:
                global connected_clients_count
                header   = self.client.recv(7)
                packetid = int.from_bytes(header[:2], 'big')
                length   = int.from_bytes(header[2:5], 'big')
                version  = int.from_bytes(header[5:], 'big')
                data     = self.recvall(length)
                LobbyInfoMessage(self.device, self.player, connected_clients_count).Send()
                if len(header) >= 7:
                    if length == len(data):
                        print('[*] {} received'.format(packetid))

                        try:
                            if self.usedCryptography == "RC4":
                                decrypted = self.device.decrypt(data)
                            elif self.usedCryptography == "NACL":
                                decrypted = self.nacl.decrypt(packetid, data)
                            else:
                                decrypted = data
                            if packetid in availablePackets:
                                Message = availablePackets[packetid](decrypted, self.device, self.player)
                                Message.decode()
                                Message.process()
                                if packetid == 10101:
                                    Networking.Clients["Clients"][str(self.player.low_id)] = {"SocketInfo": self.client}
                                    Networking.Clients["ClientCounts"] = connected_clients_count
                                    self.device.ClientDict = Networking.Clients
                            else:
                                if self.debug:

                                    TeamErrorMessage(self.device, self.player, 69).Send()
                                    print('[*] {} not handled'.format(packetid))
                        except:
                            if self.debug:
                                TeamErrorMessage(self.device, self.player, 69).Send()

                                print('[*] Error while decrypting / handling {}'.format(packetid))
                                traceback.print_exc()
                    else:
                        print('[*] Incorrect Length for packet {} (header length: {}, data length: {})'.format(packetid, length, len(data)))
                else:
                    if self.debug:
                        print('[*] Received an invalid packet from client')
                    self.client.close()
                    break
        finally:

            #global connected_clients_count

            with client_count_lock:
                connected_clients_count -= 1
                try:
                    del Networking.Clients["Clients"][str(self.player.low_id)]
                except:
                    pass
                Networking.Clients["ClientCounts"] = connected_clients_count
                self.device.ClientDict = Networking.Clients
                print(f"Connected clients: {connected_clients_count}")
