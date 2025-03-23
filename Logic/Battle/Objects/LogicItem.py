import math
from Logic.Battle.Objects.LogicGameObjectServer import LogicGameObjectServer
import time
from Utils.BitStream import BitStream
#from Packets.Messages.Server.VisionUpdateMessage import VisionUpdateMessage
class LogicItem(BitStream):
    def __init__(self, device):
        self.device = device
        
    def encode(player, stream, heroes, index):
        LogicGameObjectServer.encode(stream,heroes["objectInfos"])

    def tick(self, player, db):
        battleInfo = db.getBattleInfo([player.battleID])[0]
        items_to_remove = [] 

        for index, array in list(battleInfo["gameObjects"]["gameObjects"]["items"].items()):
            for index1, array in battleInfo["gameObjects"]["gameObjects"]["heroes"].items():
                distance = math.sqrt(
                    (battleInfo["gameObjects"]["gameObjects"]["items"][index]["objectInfos"]["x"] - 
                    battleInfo["gameObjects"]["gameObjects"]["heroes"][index1]["objectInfos"]["x"]) ** 2 
                    +
                    (battleInfo["gameObjects"]["gameObjects"]["items"][index]["objectInfos"]["y"] - 
                    battleInfo["gameObjects"]["gameObjects"]["heroes"][index1]["objectInfos"]["y"]) ** 2
                )

                if distance <= 200:
                    LogicItem(self.device).collect(player, db, battleInfo, index, index1)
                    break


        
            
    def collect(self, player, db, battleInfo, itemindex, playerindex):
        playerInfos = battleInfo["gameObjects"]["gameObjects"]["heroes"][playerindex]["objectInfos"]
        

        itemInfos = battleInfo["gameObjects"]["gameObjects"]["items"][itemindex]["objectInfos"]
        if itemInfos is None:
            return 

        start_x, start_y = itemInfos["x"], itemInfos["y"]
        
        for i in range(3):  
            t = i / 2
            itemInfos["x"] = int((1 - t) * start_x + t * playerInfos["x"])
            itemInfos["y"] = int((1 - t) * start_y + t * playerInfos["y"])
            itemInfos["z"] = int(250 * (1 - (2 * (t - 0.5)) ** 2))
            
            db.updateBattle(player.battleID, battleInfo)  

        battleInfo["gameObjects"]["gameObjects"]["items"].pop(itemindex, None)
        battleInfo["gameObjects"]["csvIDArray"].pop("7", None)
        battleInfo["gameObjects"]["indexArray"].pop("7", None) 
        battleInfo["gameObjects"]["count"] -= 1 
        battleInfo["killArray"][playerindex]["score"]+=1
        battleInfo["gameObjects"]["gameObjects"]["heroes"][playerindex]["itemsAmount"] += 1
        
        db.updateBattle(player.battleID, battleInfo)
