from Utils.Writer import Writer
from Logic.Player import Player
from Packets.ServerCommandsFactory import commands

class AvailableServerCommandMessage(Writer):
     def __init__(self, device, player, commandID):
        super().__init__(device)
        self.player = player
        self.id = 24111
        self.device = device
        self.commandID = commandID

     def encode(self):
        if self.commandID in commands:
            self.writeVInt(self.commandID)
            commands[self.commandID].encode(self)
            
        else:
            print("[*] Unable to create ", self.commandID)