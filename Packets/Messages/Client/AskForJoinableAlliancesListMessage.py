from Packets.Messages.Server.JoinableAlliancesListMessage import JoinableAlliancesListMessage
from Utils.Reader import ByteStream
from Logic.Player import Player


class AskForJoinableAlliancesListMessage(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        pass

    def process(self):
        JoinableAlliancesListMessage(self.device, self.player).Send() # 14109