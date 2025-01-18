from Utils.Writer import Writer
from Entries.StreamEntry import StreamEntry
from Entries.PlayerDisplayData import PlayerDisplayData
from Database.DatabaseManager import DataBase

class JoinRequestAllianceStreamEntry:
    def encode(self: Writer, info):
        db = DataBase(self.player)
        StreamEntry.encode(self, info)
        playerToken = db.getTokenByLowId(info["PlayerID"])
        playersData = db.getSpecifiedPlayers([playerToken])
        playerData = playersData[0]
        self.writeString(info["Message"]) # promotion message
        self.writeString(info["PlayerName"]) # who accepted/rejected the player
        self.writeVInt(info["Event"]) # state (0: rejected, 1: pending, 2: accepted)
        self.writeVInt(0) # little thing wrote on pfp wth
        self.writeDataReference(28, playerData["profile_icon"]) # player pfp

