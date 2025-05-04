from Packets.Messages.Server.MatchMakingStatusMessage import MatchMakingStatusMessage
from Packets.Messages.Server.StartLoadingMessage import StartLoadingMessage
from Utils.Reader import ByteStream
from Logic.Player import Player
from Logic.Battle.LogicBattle import LogicBattle
from Packets.Messages.Server.UDPConnectionInfoMessage import UDPConnectionInfoMessage
import time
from Database.DatabaseManager import DataBase
import json
import math 
class MatchmakeRequestMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player
        self.settings = json.load(open('Settings.json'))

    def decode(self):
        self.readVInt()
        self.CardID = self.readDataReference() # Selected card
        self.MapIndex = self.readVInt() # Event Index
        self.readVInt() # Event Index
        self.readVInt() # Highstakes Index
        self.readVInt()
        self.player.brawler_id = self.CardID[1]
        

    def process(self):
        
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
        """
        stripped until i fix
        while True:
            elapsed_time = time.time() - matchmakingData["startedTime"] 
            remaining_time = 20 - elapsed_time 

            if remaining_time <= 0:
                break

            display_time = math.floor(remaining_time)
            if display_time != math.floor(remaining_time + 0.1):  
                matchmakingData["displayTIme"] = display_time
        """
        try:
            db.createBattle()
        except:
            pass
        
        StartLoadingMessage(self.device, self.player).Send()
        
        
        if self.settings["UseUDPServer"]:
            UDPConnectionInfoMessage(self.device, self.player).Send() # its broken so please keep tcp
        else:
            battle = LogicBattle(self.device, self.player)
            battle.start()