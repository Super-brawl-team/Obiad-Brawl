from Packets.Messages.Server.TeamMessage import TeamMessage
from Logic.Player import Player
from Utils.Reader import ByteStream


class TeamSetLocationMessage(ByteStream):
    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = Player(device)


    def decode(self):
        LocationID = self.read_Vint()
        MapID = self.read_Vint()
            

    def process(self):
        TeamMessage(self.device, self.player).Send()