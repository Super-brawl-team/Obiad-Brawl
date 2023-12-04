from Logic.Player import Player
from Packets.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage

from Utils.Reader import ByteStream

class LogicGatchaCommand(ByteStream):
    def __init__(self, device, player, data):
        super().__init__(data)
        self.player = player
        self.device = device

    def decode(self):
        pass

    def process(self):
        AvailableServerCommandMessage(self.device, self.player, 203).Send()