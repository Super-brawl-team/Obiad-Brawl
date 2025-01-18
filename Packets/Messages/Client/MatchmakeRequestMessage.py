from Packets.Messages.Server.MatchMakingStatusMessage import MatchMakingStatusMessage
from Packets.Messages.Server.StartLoadingMessage import StartLoadingMessage
from Utils.Reader import ByteStream
from Logic.Player import Player
from Logic.Battle.LogicBattle import LogicBattle
from Packets.Messages.Server.UDPConnectionInfoMessage import UDPConnectionInfoMessage
import time


class MatchmakeRequestMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        self.readVInt()
        self.CardID = self.readDataReference() # Selected card
        self.MapIndex = self.readVInt() # Event Index
        self.readVInt() # Event Index
        self.readVInt() # Highstakes Index
        self.readVInt()
        

    def process(self):
        
<<<<<<< Updated upstream
        MatchMakingStatusMessage(self.device, self.player, True, self.seconds).Send()
=======
<<<<<<< HEAD
        MatchMakingStatusMessage(self.device, self.player, True, 20).Send()
=======
        MatchMakingStatusMessage(self.device, self.player, True, self.seconds).Send()
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
        UDPConnectionInfoMessage(self.device, self.player).Send()
        LogicBattle.start(self.client, self.player)