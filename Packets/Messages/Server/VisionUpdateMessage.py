from Utils.Writer import Writer
from Logic.Battle.Objects.LogicGameObjectManagerServer import LogicGameObjectManagerServer
import time
from Utils.BitStream import BitStream
from Database.DatabaseManager import DataBase

class VisionUpdateMessage(Writer):
    def __init__(self, device, player):
        self.device = device
        self.id = 24109
        self.player = player
        #self.version = 1
        super().__init__(self.device)


    def encode(self):
        db = DataBase(self.player)
        battleInfo = db.getBattleInfo([self.player.battleID])[0]
        matchmake = db.loadMatchmakingData([self.player.battleID])[0]
        self.writeVInt(matchmake["battleTicks"]) # Battle Ticks
        self.writeVInt(0) # related to wifi?
        self.writeVInt(1) # Commands Count (just dont use this lmao)
        
        stream = BitStream()
        
        LogicGameObjectManagerServer.encode(stream, 2000000, 2, 1, 2, self.player, battleInfo)
        self.writeInt(stream.getLength())
        self.buffer += stream.getByteArray()
        return self.buffer
        #self.writeBytes(stream.getByteArray(), stream.getLength())
        