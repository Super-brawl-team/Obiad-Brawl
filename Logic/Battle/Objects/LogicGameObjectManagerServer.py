import time
from Utils.BitStream import BitStream
#from Logic.Battle.Objects.TileMap import TileMap as tileMap
class LogicGameObjectManagerServer(BitStream):

    
    def encode(self, ownObjectGlobalId, playerIndex, teamIndex, gamemodeVariation, player):
        # every self.writePositiveInt(0, 1) are booleans, the first arg is the bool (0 : false, 1: true) and secon arg is bitcount
        self.writePositiveInt(2000000, 21) # global id stuffs
        self.writePositiveInt(0, 15) # fade counter
        self.writePositiveInt(1 if player.battleTicks > 900 else 0, 1) # is game finished?
        self.writePositiveInt(0, 5) # map size related
        self.writePositiveInt(14, 6) # map size related
        self.writePositiveInt(13, 5) # map size related
        self.writePositiveInt(32, 6) # map size related
        # is wall destroyed array from the pits of hell
        '''
        for i in range(tileMap.width):
            for j in range(tileMap.weight):
                tile = tileMap.GetTile(i, j, True)
                if tile.Data.RespawnSeconds > 0 or tile.Data.IsDestructible:       THATS FOR SOON
                    self.writePositiveInt(0, 1)
        '''
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1) # i try to break a wall
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        # ulti related array
        self.writePositiveInt(1, 1) # unk
        self.writePositiveInt(1, 1) # has ulti
        self.writePositiveInt(1000, 10) # ulti charge (only for your player) 1000 is full ulti
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        # ulti array end
        self.writePositiveInt(1, 3) # ig collected bounty stars
        self.writePositiveInt(1, 3) # collected bounty stars for ennemies
        # kills related array
        self.writePositiveInt(1, 6) # your bounty stars
        self.writePositiveInt(0, 2) # kills array thing
        self.writePositiveInt(5, 6) # bot 1 bounty stars
        self.writePositiveInt(0, 2)
        self.writePositiveInt(0, 6) 
        self.writePositiveInt(0, 2)
        self.writePositiveInt(0, 6)
        self.writePositiveInt(0, 2)
        self.writePositiveInt(0, 6)
        self.writePositiveInt(0, 2)
        self.writePositiveInt(20, 6)
        self.writePositiveInt(0, 2)
        # kills related array ends
        self.writePositiveInt(10, 7) # game objects count
        #  game objects ids array
        self.writePositiveInt(16, 5) # csv global id 16 is characters.csv
        self.writePositiveInt(0, 8)  # csv line (so the selected character)
        self.writePositiveInt(16, 5)
        self.writePositiveInt(3, 8)
        self.writePositiveInt(16, 5)
        self.writePositiveInt(10, 8)
        self.writePositiveInt(16, 5)
        self.writePositiveInt(10, 8)
        self.writePositiveInt(16, 5)
        self.writePositiveInt(1, 8)
        self.writePositiveInt(16, 5)
        self.writePositiveInt(7, 8)
        self.writePositiveInt(6, 5) # 6 is projectiles.csv
        self.writePositiveInt(1, 8)
        self.writePositiveInt(18, 5) # 18 is items.csv
        self.writePositiveInt(10, 8)
        self.writePositiveInt(17, 5) # 17 is area_effects.csv
        self.writePositiveInt(0, 8)
        self.writePositiveInt(16, 5)
        self.writePositiveInt(29, 8) # ball id, edit it if u changed stuffs in characters.csv
       
        # game objects ids array end
        # game objects index array
        # 1= projectile, 2 = characters, 3= area effects, 4 = items
        self.writePositiveInt(2, 5)
        self.writePositiveInt(0, 14)
        self.writePositiveInt(2, 5)
        self.writePositiveInt(1, 14)
        self.writePositiveInt(2, 5)
        self.writePositiveInt(2, 14)
        self.writePositiveInt(2, 5)
        self.writePositiveInt(3, 14)
        self.writePositiveInt(2, 5)
        self.writePositiveInt(4, 14)
        self.writePositiveInt(2, 5)
        self.writePositiveInt(5, 14)
        self.writePositiveInt(1, 5)
        self.writePositiveInt(0, 14)
        self.writePositiveInt(4, 5)
        self.writePositiveInt(0, 14)
        self.writePositiveInt(3, 5)
        self.writePositiveInt(0, 14)
        self.writePositiveInt(2, 5)
        self.writePositiveInt(6, 14)
        
        # game objects index array ends
        # game objects array 
        # your player
        self.writePositiveInt(player.x, 13) # x
        self.writePositiveInt(player.y, 14) # y
        self.writePositiveInt(0, 7) # player index
        self.writePositiveInt(100, 12) # z
        self.writePositiveInt(10, 4) # visibility
        self.writePositiveInt(0, 1) # you have that instead of rotation ting bots  has
        self.writePositiveInt(0, 3) # state(1: idk exactly, 2:has attacked, 3: has used ulti, 4: normal)
        self.writePositiveInt(1, 1) # weird state, its like boosted with the drink
        self.writePositiveInt(1, 1) # idk
        self.writePositiveInt(1, 1) # playing anim related
        self.writePositiveInt(63, 6) # played anim lol keep it 63 please
        self.writePositiveInt(0, 1) # rotation related
        self.writePositiveInt(0, 1) # stunned
        self.writePositiveInt(0, 1) # unk
        self.writePositiveInt(0, 1) # is poisonned
        self.writePositiveInt(0, 7) # idk
        self.writePositiveInt(0, 5) # idk
        self.writePositiveInt(800, 11) # current hp
        self.writePositiveInt(5000, 11) # max hp
        self.writePositiveInt(1, 7) # items amount (here its bounty stars)
        self.writePositiveInt(0, 13) #idk
        self.writePositiveInt(0, 11) # idk
        self.writePositiveInt(0, 1) # idk
        self.writePositiveInt(0, 1) # is immune
        self.writePositiveInt(0, 1) # rotate related
        self.writePositiveInt(0, 1) # dev rage activated
        self.writePositiveInt(0, 1)# aiming with ulti
        self.writePositiveInt(0, 1) # ulti activated
        self.writePositiveInt(0, 1) # invisible
        self.writePositiveInt(0, 1)  # not fully visible
        self.writePositiveInt(0, 9) # idk
        self.writePositiveInt(1, 1) # idk but its only for your player
        self.writePositiveInt(0, 9) # same
        self.writePositiveInt(1, 5) # damages count
        for x in range(1):
            self.writePositiveInt(1, 1) # why not.....
            self.writePositiveInt(1, 12) # damages dealt
        # skills array
        # attack
        self.writePositiveInt(0, 11) # active ticks
        self.writePositiveInt(0, 1) # keep it false
        self.writePositiveInt(0, 12) # unk
        self.writePositiveInt(1000, 12) # your ammos 1000 = 1 full ammo (only if max charge is higher then 0)
        # attack end
        # ulti
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 12)
        # ulti end
        # not your player anymore
        # bot 1
        self.writePositiveInt(2550, 13)
        self.writePositiveInt(9750, 14)
        self.writePositiveInt(1, 7)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(10, 4)
        self.writePositiveInt(270, 9)
        self.writePositiveInt(270, 9)
        self.writePositiveInt(4, 3)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(63, 6)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 7)
        self.writePositiveInt(0, 5)
        self.writePositiveInt(600, 11)
        self.writePositiveInt(600, 11)
        self.writePositiveInt(1, 7)
        self.writePositiveInt(0, 13)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 9)
        self.writePositiveInt(0, 5)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(3000, 12)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 12)
        # not bot 1 anymore
        # bot 2
        self.writePositiveInt(3150, 13)
        self.writePositiveInt(9750, 14)
        self.writePositiveInt(2, 7)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(10, 4)
        self.writePositiveInt(270, 9) # rotation thing only bots has
        self.writePositiveInt(270, 9) # rotation thing only bots has
        self.writePositiveInt(4, 3)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(63, 6)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 7)
        self.writePositiveInt(0, 5)
        self.writePositiveInt(1300, 11)
        self.writePositiveInt(1300, 11)
        self.writePositiveInt(1, 7)
        self.writePositiveInt(0, 13)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 9)
        self.writePositiveInt(0, 5)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(3000, 12)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 12)
        # not bot 2 anymore
        # bot 3
        self.writePositiveInt(1950, 13)
        self.writePositiveInt(150, 14)
        self.writePositiveInt(19, 7)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(10, 4)
        self.writePositiveInt(90, 9)
        self.writePositiveInt(90, 9)
        self.writePositiveInt(4, 3)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(63, 6)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 7)
        self.writePositiveInt(0, 5)
        self.writePositiveInt(1300, 11)
        self.writePositiveInt(1300, 11)
        self.writePositiveInt(1, 7)
        self.writePositiveInt(0, 13)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 9)
        self.writePositiveInt(0, 5)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(3000, 12)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 12)
        # not bot 3 anymore
        # bot 4
        self.writePositiveInt(2550, 13)
        self.writePositiveInt(150, 14)
        self.writePositiveInt(20, 7)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(10, 4)
        self.writePositiveInt(90, 9)
        self.writePositiveInt(90, 9)
        self.writePositiveInt(4, 3)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(63, 6)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 7)
        self.writePositiveInt(0, 5)
        self.writePositiveInt(600, 11)
        self.writePositiveInt(600, 11)
        self.writePositiveInt(1, 7)
        self.writePositiveInt(0, 13)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 9)
        self.writePositiveInt(0, 5)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(3000, 12)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 12)
        # not bot 4 anymore
        # bot 5
        self.writePositiveInt(3150, 13)
        self.writePositiveInt(150, 14)
        self.writePositiveInt(21, 7)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(10, 4)
        self.writePositiveInt(90, 9)
        self.writePositiveInt(90, 9)
        self.writePositiveInt(4, 3)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(63, 6)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 7)
        self.writePositiveInt(0, 5)
        self.writePositiveInt(700, 11)
        self.writePositiveInt(700, 11)
        self.writePositiveInt(1, 7)
        self.writePositiveInt(0, 13)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 9)
        self.writePositiveInt(0, 5)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(3000, 12)
        self.writePositiveInt(0, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 12)
        # not bot 5 anymore
        # shelly ulti projectile start
        self.writePositiveInt(abs(player.x - 300), 13)
        self.writePositiveInt(player.y + 300, 14)
        self.writePositiveInt(0, 7)
        self.writePositiveInt(350, 12)
        self.writePositiveInt(0, 3) # state
        self.writePositiveInt(992, 10) # path related
        self.writePositiveInt(0, 1) # idk tbh
        # shelly ulti projectile end
        # bounty star in the middle of the map
        self.writePositiveInt(2550, 13)
        self.writePositiveInt(4950, 14)
        self.writePositiveInt(102, 7)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(10, 4)
        # not bounty star in the middle of the map anymore
        # area effect test
        self.writePositiveInt(abs(player.x - 600), 13)
        self.writePositiveInt(player.y + 600, 14)
        self.writePositiveInt(102, 7)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(10, 4)
        # area effect test end
        # brawl ball xddd
        self.writePositiveInt(2550, 13)
        self.writePositiveInt(150, 14)
        self.writePositiveInt(102, 7)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(10, 4)
        self.writePositiveInt(0, 3)
        self.writePositiveInt(1, 11)
        self.writePositiveInt(1, 11)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 9)
        self.writePositiveInt(0, 5)