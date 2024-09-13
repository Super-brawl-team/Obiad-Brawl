from Logic.Player import Player
from Packets.Messages.Server.TeamMessage import TeamMessage
from Packets.Messages.Server.TeamGameStartingMessage import TeamGameStartingMessage
from Packets.Messages.Server.MatchMakingStatusMessage import MatchMakingStatusMessage
from Packets.Messages.Server.StartLoadingMessage import StartLoadingMessage
from Packets.Messages.Server.UDPConnectionInfoMessage import UDPConnectionInfoMessage
from Utils.Reader import ByteStream
from Logic.Battle.LogicBattle import LogicBattle
import time


class TeamSetMemberReadyMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player
        self.seconds = 20


    def decode(self):
        self.player.isReady = self.readBoolean()
        self.readVInt() #idk


    def process(self):
        TeamMessage(self.device, self.player).Send()
        TeamGameStartingMessage(self.device, self.player).Send()
        self.player.matchmakeStartTime = time.time()
        self.player.isReady = False
        MatchMakingStatusMessage(self.device, self.player, True, self.seconds).Send()
        UDPConnectionInfoMessage(self.device, self.player).Send()
        battle = LogicBattle(self.device, self.player)
        battle.start()
        
