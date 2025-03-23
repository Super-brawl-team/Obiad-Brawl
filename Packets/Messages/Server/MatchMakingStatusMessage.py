from Utils.Writer import Writer
import time
from Database.DatabaseManager import DataBase

class MatchMakingStatusMessage(Writer):
    def __init__(self, device, player, matchmakeState):
        self.device = device
        self.id = 20405
        self.player = player
        self.matchmakeState = matchmakeState
        super().__init__(self.device)


    def encode(self):
        db = DataBase(self.player)
        matchmakeData = db.loadMatchmakingData([self.player.battleID])[0]
        self.writeInt(matchmakeData["displayTime"]) # Matchmake Timer
        self.writeInt(len(matchmakeData["players"])) # Current Players in Matchmake
        for id in matchmakeData["players"]:
            player = db.getSpecifiedPlayers([db.getTokenByLowId(id)])[0]
            self.writeString(player["name"])
            self.writeBoolean(self.matchmakeState)
            self.writeLong(0, id)
        self.writeInt(matchmakeData["maximumPlayers"]) # Maximum Players in Matchmake
