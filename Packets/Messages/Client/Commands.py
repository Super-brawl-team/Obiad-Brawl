# -*- coding: utf-8 -*-

from Utils.Reader import ByteStream
from Utils.Writer import Writer
from Logic.Player import Player
from Packets.LogicCommandManager import commands


class Commands(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = Player(device)

    def decode(self):
<<<<<<< Updated upstream:Packets/Messages/Client/Commands.py
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.isCommand = self.read_Vint()
        if self.isCommand != 0:
            self.commandID = self.read_Vint()

    def process(self):
        if self.isCommand != 0:
            if self.commandID in commands:
                print("ECT Command handled: ", self.commandID)
                command = commands[self.commandID](self.device, self.player, self.data)
                command.decode()
                command.process()
            elif self.commandID > 0:
                print("Unhandled command: ", self.commandID)      
=======
        self.isCommand = self.readBoolean()
        self.readVInt()
        self.readVInt()
        self.commandAmount = self.readVInt()
        self.commandID = self.readVInt() 

    def process(self):
        if self.commandID in commands:
                print("[*]", self.commandID, "received")
                command = commands[self.commandID](self.device, self.player, self.data)
                command.decode()
                command.process()
        elif self.commandID > 0:
                print("[*] ", self.commandID, "not handled")  
        else:
                print("[*] A negative length command got recieved")    
>>>>>>> Stashed changes:Packets/Messages/Client/EndClientTurnMessage.py