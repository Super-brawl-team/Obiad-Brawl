from Logic.Player import Player
from Packets.Messages.Server.TeamMessage import TeamMessage
from Packets.Messages.Server.TeamGameStartingMessage import TeamGameStartingMessage
from Utils.Reader import ByteStream


class TeamSetMemberReadyMessage(ByteStream):
    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = Player(device)


    def decode(self):
        isReady = self.read_Vint()
        self.read_Vint()


    def process(self):
        TeamMessage(self.device, self.player).Send()
        TeamGameStartingMessage(self.device, self.player).Send()
        
