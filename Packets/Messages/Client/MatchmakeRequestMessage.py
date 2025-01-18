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
        
        MatchMakingStatusMessage(self.device, self.player, True, 20).Send()
        UDPConnectionInfoMessage(self.device, self.player).Send()
        LogicBattle.start(self.device, self.player)