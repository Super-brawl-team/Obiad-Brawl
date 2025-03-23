import time
from Utils.BitStream import BitStream

class LogicGameObjectServer(BitStream):

    
    def encode(stream, playerData):
        
        stream.writePositiveInt(playerData["x"], 13)
        stream.writePositiveInt(playerData["y"], 14)
        stream.writePositiveInt(playerData["index"], 7)
        stream.writePositiveInt(playerData["z"], 12)
        stream.writePositiveInt(playerData["visibility"], 4)
        