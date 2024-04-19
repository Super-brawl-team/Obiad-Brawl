from Packets.Messages.Server.TeamMessage import TeamMessage
from Utils.Reader import ByteStream
from Logic.Player import Player


class TeamToggleMemberSideMessage(ByteStream):
    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = Player(device)


    def decode(self):
        self.read_Vint() # Where player used to be
        self.read_Vint() # New place for the player
        

    def process(self):
        TeamMessage(self.device, self.player).Send()