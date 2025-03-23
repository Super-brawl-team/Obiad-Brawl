from Logic.Player import Player
from Packets.Messages.Server.TeamMessage import TeamMessage
from Packets.Messages.Server.TeamGameStartingMessage import TeamGameStartingMessage
from Packets.Messages.Server.MatchMakingStatusMessage import MatchMakingStatusMessage
from Packets.Messages.Server.StartLoadingMessage import StartLoadingMessage
from Packets.Messages.Server.UDPConnectionInfoMessage import UDPConnectionInfoMessage
from Utils.Reader import ByteStream
from Logic.Battle.LogicBattle import LogicBattle
import time
from Database.DatabaseManager import DataBase
import math
import json
class TeamSetMemberReadyMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        self.player.isReady = self.readBoolean()
        self.readVInt() #idk


    def process(self):
        TeamMessage(self.device, self.player).Send()
        TeamGameStartingMessage(self.device, self.player).Send()
        db = DataBase(self.player)
        db.createBattleID()
        db.createMatchmakingData()
        db.replaceValue("battleID", self.player.battleID)
        matchmakingData = db.loadMatchmakingData([self.player.battleID])[0]
        if self.player.low_id in matchmakingData["players"]:
            pass
        else:
            matchmakingData["players"].append(self.player.low_id)
            db.updateMatchmake(self.player.battleID, matchmakingData)
        MatchMakingStatusMessage(self.device, self.player, True).Send()
        while True:
            elapsed_time = time.time() - matchmakingData["startedTime"] 
            remaining_time = 20 - elapsed_time 

            if remaining_time <= 0:
                break

            display_time = math.floor(remaining_time)
            if display_time != math.floor(remaining_time + 0.1):  
                matchmakingData["displayTIme"] = display_time
        
        try:
            db.createBattle()
        except:
            pass
        
        StartLoadingMessage(self.device, self.player).Send()
        
        self.settings = json.load(open('Settings.json'))
        if self.settings["UseUDPServer"]:
            UDPConnectionInfoMessage(self.device, self.player).Send() # its broken so please keep tcp
        else:
            battle = LogicBattle(self.device, self.player)
            battle.start()