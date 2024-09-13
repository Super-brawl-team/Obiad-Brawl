from Utils.Writer import Writer
from Logic.Battle.Objects.LogicGameObjectManagerServer import LogicGameObjectManagerServer
import time
from Utils.BitStream import BitStream


class VisionUpdateMessage(Writer):
    def __init__(self, device, player):
        self.device = device
        self.id = 24109
        self.player = player
        self.version = 1
        super().__init__(self.device)


    def encode(self):
        self.writeVInt(self.player.battleTicks) # Battle Ticks
        self.writeVInt(0) # related to wifi?
        self.writeVInt(1) # Commands Count (just dont use this lmao)
        
        stream = BitStream()
        
        LogicGameObjectManagerServer.encode(stream, 2000000, 2, 1, 2)
        self.writeInt(stream.getLength())
        self.buffer += stream.getByteArray()
        #self.writeBytes(stream.getByteArray(), stream.getLength())
        