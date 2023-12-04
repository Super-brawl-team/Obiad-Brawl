from Packets.Messages.Server.ClanData import ClanData
from Utils.Reader import ByteStream
from Logic.Player import Player


class AskForClan(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.HighID = 0
        self.LowID = 0

    def decode(self):
        self.HighID = self.ReadUint32()
        self.LowID = self.ReadUint32()

    def process(self):
        ClanData(self.device, self.device.Player).Send() # 14109