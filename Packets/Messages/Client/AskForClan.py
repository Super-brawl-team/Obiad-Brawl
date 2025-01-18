from Packets.Messages.Server.ClanData import ClanData
from Utils.Reader import ByteStream
from Logic.Player import Player


class AskForClan(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player
        self.HighID = 0
        self.LowID = 0

    def decode(self):
        self.HighID = self.readUint32()
        self.LowID = self.readUint32()

    def process(self):
        ClanData(self.device, self.player).Send() # 14109