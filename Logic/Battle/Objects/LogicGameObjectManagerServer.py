import time
from Utils.BitStream import BitStream
from Database.DatabaseManager import DataBase
#from Logic.Battle.Objects.TileMap import TileMap as tileMap
from Logic.Battle.Objects.LogicCharacter import LogicCharacter
from Logic.Battle.Objects.LogicProjectile import LogicProjectile
from Logic.Battle.Objects.LogicAreaEffect import LogicAreaEffect
from Logic.Battle.Objects.LogicItem import LogicItem
class LogicGameObjectManagerServer(BitStream):

    
    def encode(self, ownObjectGlobalId, playerIndex, teamIndex, gamemodeVariation, player, battleInfo):

        # every self.writePositiveInt(0, 1) are booleans, the first arg is the bool (0 : false, 1: true) and secon arg is bitcount
        self.writePositiveInt(battleInfo["globalID"], 21) # global id stuffs
        self.writePositiveInt(battleInfo["fadeCounter"], 15) # fade counter
        self.writeBoolean(battleInfo["isGameOver"]) # is game finished?
        self.writePositiveInt(battleInfo["unkMapSize"], 5) # map size related
        self.writePositiveInt(battleInfo["unkMapSize2"], 6) # map size related
        self.writePositiveInt(battleInfo["tileMapWidth"], 5) # map size related
        self.writePositiveInt(battleInfo["tileMapHeight"], 6) # map size related
        # is wall destroyed array from the pits of hell
        for index, tile in battleInfo["destructibleTiles"].items():
            self.writeBoolean(battleInfo["destructibleTiles"][index]["isDestroyed"])
        # ulti related array
        for index, ulti in battleInfo["ultiArray"].items():
            self.writeBoolean(battleInfo["ultiArray"][index]["unknown"])
            self.writeBoolean(battleInfo["ultiArray"][index]["hasUlti"])
            if int(index) == 1:
                self.writePositiveInt(battleInfo["ultiArray"][index]["ultiCharge"], 10) # ulti charge (only for your player) 1000 is full ulti
            
        # ulti array end
        self.writePositiveInt(battleInfo["progressionSelf"], 3) # ig collected bounty stars
        self.writePositiveInt(battleInfo["progressionRival"], 3) # collected bounty stars for ennemies
        # kills related array
        for index, kill in battleInfo["killArray"].items():
            
            self.writePositiveInt(battleInfo["killArray"][index]["score"], 6)
            self.writePositiveInt(len(battleInfo["killArray"][index]["entry"]), 2)
            for index2, entry in battleInfo["killArray"][index]["entry"]:
                self.writePositiveInt(len(battleInfo["killArray"][index]["entry"][index2]["entry2"]), 3) # ANOTHER array
                for index3, entry in battleInfo["killArray"][index]["entry"][index2]["entry2"].items():
                    self.writePositiveInt(battleInfo["killArray"][index]["entry"][index2]["entry2"][index3]["value"], 4)
        
        # kills related array ends
        self.writePositiveInt(battleInfo["gameObjects"]["count"], 7) # game objects count
        #  game objects ids array
        for index, array in battleInfo["gameObjects"]["csvIDArray"].items():
            
            self.writePositiveInt(battleInfo["gameObjects"]["csvIDArray"][index]["classID"], 5) # csv global id 16 is characters.csv 6 is projectiles.csv 18 is items.csv 17 is area_effects.csv
            self.writePositiveInt(battleInfo["gameObjects"]["csvIDArray"][index]["instanceID"], 8)  # csv line (so the selected character)

       
        # game objects ids array end
        # game objects index array
        # 1= projectile, 2 = characters, 3= area effects, 4 = items
        for index, array in battleInfo["gameObjects"]["indexArray"].items():
                
            self.writePositiveInt(battleInfo["gameObjects"]["indexArray"][index]["classID"], 5)
            self.writePositiveInt(battleInfo["gameObjects"]["indexArray"][index]["instanceID"], 14)

        for index, array in battleInfo["gameObjects"]["gameObjects"]["heroes"].items():
            LogicCharacter.encode(player, self, battleInfo["gameObjects"]["gameObjects"]["heroes"][index], int(index))
        for index, array in battleInfo["gameObjects"]["gameObjects"]["projectiles"].items():
            LogicProjectile.encode(player, self, battleInfo["gameObjects"]["gameObjects"]["projectiles"][index], int(index))
        for index, array in battleInfo["gameObjects"]["gameObjects"]["items"].items():
            LogicItem.encode(player, self, battleInfo["gameObjects"]["gameObjects"]["items"][index], int(index))
        for index, array in battleInfo["gameObjects"]["gameObjects"]["areaEffects"].items():
            LogicAreaEffect.encode(player, self, battleInfo["gameObjects"]["gameObjects"]["areaEffects"][index], int(index))
        for index, array in battleInfo["gameObjects"]["gameObjects"]["characters"].items():
            LogicCharacter.encode(player, self, battleInfo["gameObjects"]["gameObjects"]["characters"][index], int(index))
