# -*- coding: utf-8 -*-
import os
import json
import traceback

from twisted.internet import reactor, protocol

from Logic.Device import Device
from Packets.Factory import *


class ServerHandler(protocol.Protocol, Device):

    def __init__(self, settings):
        Device.__init__(self)
        self.settings = settings
        self.buffer = b''
        self.packet = b''

    def connectionMade(self):
        '''
        Will be automatically called by twisted when
        a client connect
        '''
        client = self.transport.getPeer()
        print('[*] Got new connection from {}'.format(client.host))

    def connectionLost(self, reason):
        '''
        Will be automatically called by twisted when
        a client disconnect
        '''
        print('[*] A player has disconnected')

    def dataReceived(self, data):
        '''
        Will be automatically called by
        twisted when server receive data
        '''

        self.buffer += data
        while self.buffer:
            if self.packet:
                packetID = int.from_bytes(self.packet[:2], "big")
                packetLength = int.from_bytes(self.packet[2:5], "big")

                if len(self.buffer) >= packetLength:
                    self.packet += self.buffer[:packetLength]
                    self.processPacket(packetID, self.packet[7:])
                    self.packet = b""
                    self.buffer = self.buffer[packetLength:]

                else:
                    break

            elif len(self.buffer) >= 7:
                self.packet = self.buffer[:7]

                if len(self.buffer) == 7 and int.from_bytes(self.packet[2:5], 'big') == 0:
                    packetID = int.from_bytes(self.packet[:2], "big")
                    self.processPacket(packetID, self.packet[7:])

                self.buffer  = self.buffer[7:]


class ServerFactory(protocol.Factory):

    def __init__(self, settings):
        self.settings = settings

    def buildProtocol(self, addr):
        return ServerHandler(self.settings)


def startTwistedFactory():

    settings = json.load(open("Settings.json"))
    server = reactor.listenTCP(settings['Port'], ServerFactory(settings))
    width  = os.get_terminal_size().columns

    print('Twisted server is listening on {}:{}'.format(server.getHost().host, server.getHost().port).center(width))
    print('{}'.format('-' * (width // 2)).center(width))

    reactor.run()
