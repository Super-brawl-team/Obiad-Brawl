import time
from Utils.BitStream import BitStream

class LogicGameObjectManagerServer(BitStream):

    
    def encode(stream, ownObjectGlobalId, playerIndex, teamIndex, gamemodeVariation):
        stream.writePositiveIntMax2097151(ownObjectGlobalId) # Own object global id
        stream.writePositiveIntMax32767(0)
        stream.writeBoolean(False)
        if gamemodeVariation == 6:
             stream.writePositiveIntMax63(0)
             stream.writePositiveIntMax127(14) # unk
             stream.writePositiveIntMax63(13) # tilemap width (incorrect size, i'll find correct one later)
             stream.writePositiveIntMax127(32) # tilemap height (incorrect size, i'll find correct one later)
        else:
            stream.writePositiveIntMax31(0)
            stream.writePositiveIntMax63(14) # unk
            stream.writePositiveIntMax31(13) # tilemap width
            stream.writePositiveIntMax63(32) # tilemap height

        for tileMap in range(13 + 14):
            stream.writeBoolean(False)
        
        stream.writeBoolean(True)
        stream.writeBoolean(False) # has ulti
        stream.writePositiveIntMax1023(0) # ulti related
        stream.writeBoolean(True)
        stream.writeBoolean(False)
        stream.writeBoolean(True)
        stream.writeBoolean(False)
        stream.writeBoolean(True)
        stream.writeBoolean(False)
        stream.writeBoolean(True)
        stream.writeBoolean(False)
        stream.writeBoolean(True)
        stream.writeBoolean(False)
        if gamemodeVariation == 2:
            stream.writePositiveIntMax127(0) # your side chest
            stream.writePositiveIntMax157(100) # ennemy side chest
        elif gamemodeVariation == 6:
            stream.writePositiveIntMax15(2) # players left in showdown
        
        for x in range(6):
            stream.writePositiveIntMax63(0)
            stream.writePositiveIntMax3(0)
        
        stream.writePositiveIntMax127(9) # Game objects amount

        for x in range(6):
            stream.writeDataReference(16, x) # brawlers

        stream.writeDataReference(16, 22) # safe 2
        stream.writeDataReference(16, 25) # tnt
        stream.writeDataReference(16, 25) # tnt

        for index in range(9):
            stream.writeObjectRunning(2, index)

        stream.writePositiveIntMax8191(1950) # x
        stream.writePositiveIntMax16383(9750) # y
        stream.writePositiveIntMax127(0) # index of player
        stream.writePositiveIntMax4095(0) # z? wtf is this lmao
        stream.writePositiveIntMax15(10) # visibility
        stream.writeBoolean(False) # boolean only if you play this object else its angles
        stream.writePositiveIntMax8(4) # state? hmm
        stream.writeBoolean(False)
        stream.writeBoolean(False)
        stream.writeBoolean(True)
        stream.writePositiveIntMax63(63) # playing anim ????????? what?
        stream.writeBoolean(False) # i heard its related to rotation
        stream.writeBoolean(False) # is stunned
        stream.writeBoolean(False) # idk
        stream.writeBoolean(False) # has star power (yes it exists since v1)
        stream.writePositiveIntMax127(0)
        stream.writePositiveIntMax31(0)
        stream.writePositiveIntMax2047(1500) # current health
        stream.writePositiveIntMax2047(1500) # max heealth
        stream.writePositiveIntMax63(0) # items count ?
        stream.writePositiveIntMax8191(0)
        stream.writePositiveIntMax2047(0)
        stream.writeBoolean(False)
        stream.writeBoolean(False) # is immune
        stream.writeBoolean(False)
        stream.writeBoolean(False)
        stream.writeBoolean(False)
        stream.writeBoolean(False)
        stream.writeBoolean(False)
        stream.writeBoolean(False) # not fully visible?
        stream.writePositiveIntMax511(0)
        stream.writeBoolean(True)
        stream.writePositiveIntMax511(0)
        stream.writePositiveIntMax31(1) # recieved damages count xdd
        for x in range(1):
            stream.writePositiveIntMax4095(1) # recieved damage xd
        # skills related part
        stream.writePositiveIntMax2047(0) # active ticks ig
        stream.writeBoolean(False)
        stream.writePositiveIntMax4095(0)
        stream.writePositiveIntMax4095(3000) # definitivly ammo charge
        # no more skills related
        stream.writePositiveIntMax2047(0)
        stream.writeBoolean(False)
        stream.writePositiveIntMax4095(0)
        # second player
        
        stream.writePositiveInt(2550, 13) # x
        stream.writePositiveInt(9750, 14) # y
        stream.writePositiveInt(1, 7) # player index
        stream.writePositiveInt(0, 12) # z
        stream.writePositiveInt(10, 4) # visibility
        stream.writePositiveInt(270, 9) # angle
        stream.writePositiveInt(270, 9) # angle
        stream.writePositiveInt(4, 3) # object state...
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(63, 6) # playing anim
        stream.writePositiveInt(0, 1) # rotation related
        stream.writePositiveInt(0, 1) # stunned
        stream.writePositiveInt(0, 1) # unk
        stream.writePositiveInt(0, 1) # star power
        stream.writePositiveInt(0, 7)
        stream.writePositiveInt(0, 5)
        stream.writePositiveInt(600, 11) # current health
        stream.writePositiveInt(600, 11) # max health
        stream.writePositiveInt(0, 6) # items count?
        stream.writePositiveInt(0, 13)
        stream.writePositiveInt(0, 11)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1) # has immunity shield
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1) # is fully visible ?
        stream.writePositiveInt(0, 9)
        stream.writePositiveInt(1, 5) # damages count
        for x in range(1):
            stream.writePositiveIntMax4095(1)
        # skills related
        stream.writePositiveInt(0, 11)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 12)
        stream.writePositiveInt(3000, 12) # ammo charge ?
        # end
        stream.writePositiveInt(0, 11)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 12)
        # third player
        stream.writePositiveInt(3150, 13)
        stream.writePositiveInt(9750, 14)
        stream.writePositiveInt(2, 7)
        stream.writePositiveInt(0, 12)
        stream.writePositiveInt(10, 4)
        stream.writePositiveInt(270, 9)
        stream.writePositiveInt(270, 9)
        stream.writePositiveInt(4, 3)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(63, 6)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 7)
        stream.writePositiveInt(0, 5)
        stream.writePositiveInt(700, 11)
        stream.writePositiveInt(700, 11)
        stream.writePositiveInt(0, 6)
        stream.writePositiveInt(0, 13)
        stream.writePositiveInt(0, 11)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 9)
        stream.writePositiveInt(0, 5)
        stream.writePositiveInt(0, 11)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 12)
        stream.writePositiveInt(3000, 12)
        stream.writePositiveInt(0, 11)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 12)
        # fourth player
        stream.writePositiveInt(750, 13)
        stream.writePositiveInt(150, 14)
        stream.writePositiveInt(19, 7)
        stream.writePositiveInt(0, 12)
        stream.writePositiveInt(10, 4)
        stream.writePositiveInt(90, 9)
        stream.writePositiveInt(90, 9)
        stream.writePositiveInt(4, 3)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(63, 6)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 7)
        stream.writePositiveInt(0, 5)
        stream.writePositiveInt(1300, 11)
        stream.writePositiveInt(1300, 11)
        stream.writePositiveInt(0, 6)
        stream.writePositiveInt(0, 13)
        stream.writePositiveInt(0, 11)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 9)
        stream.writePositiveInt(0, 5)
        stream.writePositiveInt(0, 11)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 12)
        stream.writePositiveInt(3000, 12)
        stream.writePositiveInt(0, 11)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 12)
        # fifth player
        stream.writePositiveInt(150, 13)
        stream.writePositiveInt(150, 14)
        stream.writePositiveInt(20, 7)
        stream.writePositiveInt(0, 12)
        stream.writePositiveInt(10, 4)
        stream.writePositiveInt(90, 9)
        stream.writePositiveInt(90, 9)
        stream.writePositiveInt(4, 3)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(63, 6)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 7)
        stream.writePositiveInt(0, 5)
        stream.writePositiveInt(700, 11)
        stream.writePositiveInt(700, 11)
        stream.writePositiveInt(0, 6)
        stream.writePositiveInt(0, 13)
        stream.writePositiveInt(0, 11)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 9)
        stream.writePositiveInt(0, 5)
        stream.writePositiveInt(0, 11)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 12)
        stream.writePositiveInt(3000, 12)
        stream.writePositiveInt(0, 11)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 12)
        # chest
        stream.writePositiveInt(2550, 13) # box x
        stream.writePositiveInt(1050, 14) # box y
        stream.writePositiveInt(22, 7) # item index... why is it so hight
        stream.writePositiveInt(0, 12) # box z
        stream.writePositiveInt(10, 4) # box visibility
        stream.writePositiveInt(4, 3) # box state
        stream.writePositiveInt(5400, 13) # box current hp
        stream.writePositiveInt(5500, 13) # box max hp
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 9)
        stream.writePositiveInt(1, 5) # box damage count
        for x in range(1):
            stream.writePositiveIntMax4095(100)
        # tnt box 1
        stream.writePositiveInt(3150, 13)
        stream.writePositiveInt(1950, 14)
        stream.writePositiveInt(22, 7)
        stream.writePositiveInt(0, 12)
        stream.writePositiveInt(10, 4)
        stream.writePositiveInt(4, 3)
        stream.writePositiveInt(3000, 13)
        stream.writePositiveInt(3000, 13)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 9)
        stream.writePositiveInt(0, 5)
        # tnt box 2
        stream.writePositiveInt(1950, 13)
        stream.writePositiveInt(1950, 14)
        stream.writePositiveInt(22, 7)
        stream.writePositiveInt(0, 12)
        stream.writePositiveInt(10, 4)
        stream.writePositiveInt(4, 3)
        stream.writePositiveInt(3000, 13)
        stream.writePositiveInt(3000, 13)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 9)
        stream.writePositiveInt(0, 5)