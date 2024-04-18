from Packets.Messages.Server.TeamMessage import TeamMessage
import random
from Logic.Player import Player
from Utils.Reader import ByteStream


class TeamCreateMessage(BSMessageReader):
    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = Player(device)


    def decode(self):
        EventSlotIndex = self.read_Vint()
        self.read_Vint()


    def process(self):
        self.player.teamID = random.randint(1, 2147483647)
        TeamMessage(self.device, self.player).Send()