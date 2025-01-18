# -*- coding: utf-8 -*-
import traceback
import json
from Cryptography.rc4 import CryptoRc4
from Packets.Factory import *
from Cryptography.nacl import NaCl

class Device:

    AndroidID = None
    DeviceModel = None
    OpenUDID = None
    OSVersion = None
    IsAndroid = False
    Language = None

    Player = None

    BattleEndType = 0
    rank = 0
    bcsv = 0
    brawler = 0
    scsv = 0
    skin = 0
    skin_id = 0
    team = 0
    PName = ""
    battle_result = 0
    game_type = 0
    rank = 0
    team = 0
    isReady = 0
    result = 0
    mmplayers = 0
    players = 0
    skin = 0
    battle_tick = 0
    bot1 = 0
    bot1_n = None
    bot2 = 0
    bot2_n = None
    bot3 = 0
    bot3_n = None
    bot4 = 0
    bot4_n = None
    bot5 = 0
    bot5_n = None
    bot6 = 0
    bot6_n = None
    bot7 = 0
    bot7_n = None
    bot8 = 0
    bot8_n = None
    bot9 = 0
    bot9_n = None

    def __init__(self, socket=None):

        self.socket = socket
        self.crypto = CryptoRc4()
        self.nacl = NaCl()
        self.settings = json.load(open('Settings.json'))
        self.usedCryptography = self.settings["usedCryptography"]

    def SendData(self, ID, data, version=None):
        if self.usedCryptography == "RC4":
         encrypted = self.crypto.encrypt(data)
        elif self.usedCryptography == "NACL":
         encrypted = self.nacl.encrypt(ID, data)
        else:
         encrypted = data
        packetID   = ID.to_bytes(2, 'big')

        if version:
            packetVersion = version.to_bytes(2, 'big')

        else:
            packetVersion = (0).to_bytes(2, 'big')

        if self.socket is None:
            self.transport.write(packetID + len(encrypted).to_bytes(3, 'big') + packetVersion + encrypted)

        else:
            self.socket.send(packetID + len(encrypted).to_bytes(3, 'big') + packetVersion + encrypted)
        
    def decrypt(self, data):
        return self.crypto.decrypt(data)

    def processPacket(self, packetID, payload):

        print('[*] {} received'.format(packetID))

        try:
            decrypted = self.decrypt(payload)

            if packetID in availablePackets:

                Message = availablePackets[packetID](decrypted, self)
                Message.decode()
                Message.process()

            else:
                print('[*] {} not handled'.format(packetID))

        except:
            print('[*] Error while decrypting / handling {}'.format(packetID))
            traceback.print_exc()
