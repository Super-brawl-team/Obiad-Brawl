from Packets.Messages.Server.VisionUpdateMessage import VisionUpdateMessage
from Packets.Messages.Server.StartLoadingMessage import StartLoadingMessage
from Packets.Messages.Client.ForceSendBattleEnd import ForceSendBattleEnd
from Packets.Messages.Server.UDPConnectionInfoMessage import UDPConnectionInfoMessage
import copy
import time
import math
from threading import Thread
from Database.DatabaseManager import DataBase
from Logic.Battle.Objects.LogicItem import LogicItem
from Logic.Battle.LogicGameModeUtil import LogicGameModeUtil
class LogicBattle(Thread):
    
    def __init__(self, device, player):
        Thread.__init__(self)
        self.device = device
        self.player = player
        self.player.battleTicks = 0
        self.started = True
    
    def run(self):
        self.startBattle()
    
    def startBattle(self):
        db = DataBase(self.player)
        matchmakingData = db.loadMatchmakingData([self.player.battleID])[0]
        self.started = True
        self.timestamp = time.time()
        while self.started:
           if matchmakingData["battleTicks"] > LogicGameModeUtil.getBattleTicks(3):
              matchmakingData["battleTicks"] = 0
              db.updateMatchmake(self.player.battleID, matchmakingData)
              self.started = False
              
              ForceBattleEnd = ForceSendBattleEnd(self.device, self.player)
              ForceBattleEnd.decode()
              ForceBattleEnd.process()
              db.clearMatchmake(self.player.battleID)
              db.clearBattle(self.player.battleID)
              self.player.battleID = 0
              db.replaceValue("battleID", self.player.battleID)
              
              break
           else:
                if time.time() - self.timestamp >= 0.05:
                    matchmakingData["battleTicks"] += 1
                    db.updateMatchmake(self.player.battleID, matchmakingData)
                    self.timestamp = time.time()
                    self.process()
                
                time.sleep(0.05)

    
    def process(self):
        db = DataBase(self.player)
        LogicItem(self.device).tick(self.player, db)
        VisionUpdateMessage(self.device, self.player).Send()