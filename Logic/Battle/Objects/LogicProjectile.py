import math
import time
from Utils.BitStream import BitStream
#from Packets.Messages.Server.VisionUpdateMessage import VisionUpdateMessage
class LogicProjectile(BitStream):
    def __init__(self, device):
        self.device = device
        
    def encode(player, stream, heroes, index):
        
        stream.writePositiveInt(abs(player.x - 300), 13)
        stream.writePositiveInt(player.y + 300, 14)
        stream.writePositiveInt(0, 7)
        stream.writePositiveInt(350, 12)
        stream.writePositiveInt(0, 3) # state
        stream.writePositiveInt(992, 10) # path related
        stream.writePositiveInt(0, 1) # idk tbh
