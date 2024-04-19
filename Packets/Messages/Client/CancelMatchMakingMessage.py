from Packets.Messages.Server.MatchMakingStatusMessage import MatchMakingStatusMessage
from Utils.Reader import ByteStream
from Logic.Player import Player


class CancelMatchMakingMessage(ByteStream):
    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)


    def decode(self):
        pass
        

    def process(self):
        MatchMakingStatusMessage(self.device, self.player, False).Send()