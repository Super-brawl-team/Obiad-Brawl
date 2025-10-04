from Utils.Writer import Writer
from Logic.Player import Player
from Packets.ServerCommandsFactory import commands

class AvailableServerCommandMessage(Writer):
     def __init__(self, device, player, commandID, data = None):
        super().__init__(device)
        self.player = player
        self.id = 24111
        self.device = device
        self.data = data
        self.commandID = commandID

     def encode(self):
        if self.commandID in commands:
            self.writeVInt(self.commandID)
            if not self.data:
                commands[self.commandID].encode(self)
            else:
                commands[self.commandID].encode(self, self.data)
            
        else:
            print("[*] Unable to create ", self.commandID)