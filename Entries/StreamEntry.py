from Utils.Writer import Writer
import time
from Database.DatabaseManager import DataBase
from Logic.Player import Player

class StreamEntry:
    def encode(ByteStream: Writer, info):
        db = DataBase(ByteStream.player)
        ByteStream.writeLogicLong(0, info["Tick"]) # StreamEntryID
        ByteStream.writeLogicLong(0, info["PlayerID"]) # TargetID
        playertoken = db.getTokenByLowId(info["PlayerID"])
        playersData = db.getSpecifiedPlayers([playertoken])
        playerData = playersData[0]
        ByteStream.writeString(playerData['name'])
        try:
            ByteStream.writeVInt(info['PlayerRole'])
        except:
            ByteStream.writeVInt(0)
        ByteStream.writeVInt(int(time.time() - info['TimeStamp']))
        ByteStream.writeBoolean(False)

