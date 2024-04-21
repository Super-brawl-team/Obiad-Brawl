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
    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = Player(device)


    def decode(self):
        self.player.isReady = self.readboolean()
        self.read_Vint() #idk


    def process(self):
        TeamMessage(self.device, self.player).Send()
        TeamGameStartingMessage(self.device, self.player).Send()
        self.player.matchmakeStartTime = time.time()
        while self.player.matchmakeStartTime - time.time() != 20: 
            for time in range(20):
                if self.player.matchmakeStartTime - time.time() >= time and self.player.matchmakeStartTime - time.time() << time + 1:
                    self.seconds = time
                    time += 1
            MatchMakingStatusMessage(self.device, self.player, True, self.seconds).Send()
        UDPConnectionInfoMessage(self.device, self.player).Send()
        LogicBattle.start(self.client, self.player)
        
