from Utils.Writer import Writer
from Logic.Battle.LogicGameObjectManagerServer import LogicGameObjectManagerServer
import time
from Utils.BitStream import BitStream


class VisionUpdate(Writer):
    def __init__(self, device, player):
        self.device = device
        self.id = 24109
        self.player = player
        super().__init__(self.device)


    def encode(self):
        self.writeVInt(self.player.battleTicks) # Battle Ticks
        self.writeVInt(self.player.wifi) # related to wifi?
        self.writeVInt(0) # Commands Count (just dont use this lmao)
        
        stream = BitStream()
        
        LogicGameObjectManagerServer.encode(stream, 2000000, 2, 1, 2)
        
        self.writeBytes(stream.getBuff())
        