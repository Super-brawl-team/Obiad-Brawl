from Packets.Messages.Server.TeamMessage import TeamMessage
import random
from Logic.Player import Player
from Utils.Reader import ByteStream


class TeamSpectateMessage(ByteStream):
    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = Player(device)


    def decode(self):
        self.player.teamID = self.read_Vint()
        self.read_Vint()
        self.read_Vint()


    def process(self):
        TeamMessage(self.device, self.player).Send()