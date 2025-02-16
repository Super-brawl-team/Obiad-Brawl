from Packets.Messages.Server.AllianceData import AllianceData
from Utils.Reader import ByteStream
from Logic.Player import Player


class AskForClan(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.ID = self.readLong()

    def process(self):
        AllianceData(self.device, self.player, self.ID[1]).Send() # 14109