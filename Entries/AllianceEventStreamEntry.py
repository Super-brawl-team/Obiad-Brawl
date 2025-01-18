from Utils.Writer import Writer
from Entries.StreamEntry import StreamEntry
from Database.DatabaseManager import DataBase
from Logic.Player import Player
class AllianceEventStreamEntry:
    def encode(self: Writer, info):
        db = DataBase(self.player)
        StreamEntry.encode(self, info)
        
        self.writeVInt(info['Event'])
        self.writeBoolean(True)
        self.writeLogicLong(0, info["targetID"])
        playertoken = db.getTokenByLowId(info["targetID"])
        playersData = db.getSpecifiedPlayers([playertoken])
        playerData = playersData[0]
        self.writeString(playerData['name'])

