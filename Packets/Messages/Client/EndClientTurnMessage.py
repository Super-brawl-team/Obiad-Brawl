# -*- coding: utf-8 -*-

from Utils.Reader import ByteStream
from Utils.Writer import Writer
from Logic.Player import Player
from Packets.LogicCommandManager import commands


class EndClientTurnMessage(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.isCommand = self.readVInt()
        if self.isCommand != 0:
            self.commandID = self.readVInt()

    def process(self):
        if self.isCommand != 0:
            if self.commandID in commands:
                print("[*]", self.commandID, "received")
                command = commands[self.commandID](self.device, self.player, self.data)
                command.decode()
                command.process()
            elif self.commandID > 0:
                print("[*] ", self.commandID, "not handled")  
            else:
                print("[*] A negative length command got recieved")    