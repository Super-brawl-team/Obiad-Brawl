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
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
=======
<<<<<<<< HEAD:Packets/Messages/Client/Commands.py
<<<<<<< Updated upstream:Packets/Messages/Client/Commands.py
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.isCommand = self.read_Vint()
========
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.isCommand = self.readVInt()
>>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b:Packets/Messages/Client/EndClientTurnMessage.py
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
<<<<<<<< HEAD:Packets/Messages/Client/Commands.py
                print("Unhandled command: ", self.commandID)      
=======
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
        self.isCommand = self.readBoolean()
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
            else:
                print("[*] A negative length command got recieved")    
=======
        else:
<<<<<<< HEAD
                print("[*] A negative length command got recieved")    
=======
                print("[*] A negative length command got recieved")    
>>>>>>> Stashed changes:Packets/Messages/Client/EndClientTurnMessage.py
========
                print("[*] ", self.commandID, "not handled")  
            else:
                print("[*] A negative length command got recieved")    
>>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b:Packets/Messages/Client/EndClientTurnMessage.py
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
