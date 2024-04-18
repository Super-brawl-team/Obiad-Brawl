from Packets.Messages.Server.TeamMessage import TeamMessage
from Utils.Reader import ByteStream
from Logic.Player import Player


class TeamChangeMemberSettingsMessage(ByteStream):
    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = Player(device)


    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.brawlerID = self.read_Vint()


    def process(self):
        TeamMessage(self.device, self.player).Send()