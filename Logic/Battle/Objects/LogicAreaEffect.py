import math
import time
from Utils.BitStream import BitStream
#from Packets.Messages.Server.VisionUpdateMessage import VisionUpdateMessage
class LogicAreaEffect(BitStream):
    def __init__(self, device):
        self.device = device
        
    def encode(player, stream, heroes, index):
        
        stream.writePositiveInt(abs(player.x - 600), 13)
        stream.writePositiveInt(player.y + 600, 14)
        stream.writePositiveInt(102, 7)
        stream.writePositiveInt(0, 12)
        stream.writePositiveInt(10, 4)
