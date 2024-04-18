from Packets.Messages.Server.MatchMakingStatusMessage import MatchMakingStatusMessage
from Utils.Reader import ByteStream
from Logic.Player import Player


class MatchmakeRequestMessage(ByteStream):
    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)


    def decode(self):
        self.read_Vint()
        self.CardID = self.readDataReference() # Selected card
        self.MapIndex = self.read_Vint() # Event Index
        self.read_Vint() # Event Index
        self.read_Vint() # Highstakes Index
        self.read_Vint()
        

    def process(self):
        MatchMakingStatusMessage(self.device, self.player, True).send()