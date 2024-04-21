from Packets.Messages.Server.MatchMakingStatusMessage import MatchMakingStatusMessage
from Packets.Messages.Server.StartLoadingMessage import StartLoadingMessage
from Utils.Reader import ByteStream
from Logic.Player import Player
from Logic.LogicBattle import LogicBattle
from Packets.Messages.Server.UDPConnectionInfoMessage import UDPConnectionInfoMessage
import time


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
        self.player.matchmakeStartTime = time.time()
        while self.player.matchmakeStartTime - time.time() != 20: 
            for time in range(20):
                if self.player.matchmakeStartTime - time.time() >= time and self.player.matchmakeStartTime - time.time() << time + 1:
                    self.seconds = time
                    time += 1
            MatchMakingStatusMessage(self.device, self.player, True, self.seconds).Send()
        UDPConnectionInfoMessage(self.device, self.player).Send()
        LogicBattle.start(self.client, self.player)