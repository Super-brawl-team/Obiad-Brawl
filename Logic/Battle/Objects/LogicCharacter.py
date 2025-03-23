import math
import time
from Logic.Battle.Objects.LogicGameObjectServer import LogicGameObjectServer
#from Packets.Messages.Server.VisionUpdateMessage import VisionUpdateMessage
from Utils.BitStream import BitStream
class LogicCharacter(BitStream):
    def __init__(self, device):
        self.device = device
        
    def encode(player, stream, heroes, index):
        LogicGameObjectServer.encode(stream,heroes["objectInfos"])
        if index == 1:
            stream.writePositiveInt(0, 1) # you have that instead of rotation ting bots  has
        else:
            stream.writePositiveInt(heroes["teamRotation"], 9) # rotation self side
            stream.writePositiveInt(heroes["ennemyRotation"], 9) # rotation ennem side
        stream.writePositiveInt(heroes["state"], 3) # state(1: idk exactly, 2:has attacked, 3: has used ulti, 4: normal)
        stream.writeBoolean(heroes["slowed"]) # weird state, its like boosted with the drink
        stream.writeBoolean(heroes["unknown"]) # idk
        stream.writeBoolean(heroes["playingAnAnimation"]) # playing anim related
        stream.writePositiveInt(heroes["playedAnimation"], 6) # played anim lol keep it 63 please
        stream.writeBoolean(heroes["rotationRelated"]) # rotation related
        stream.writeBoolean(heroes["stunned"]) # stunned
        stream.writeBoolean(heroes["unknown2"]) # unk
        stream.writeBoolean(heroes["isPoisonned"]) # is poisonned
        stream.writePositiveInt(heroes["unknown3"], 7) # idk
        stream.writePositiveInt(heroes["unknown4"], 5) # idk
        stream.writePositiveInt(heroes["currentHP"], 11) # current hp
        stream.writePositiveInt(heroes["maximumHP"], 11) # max hp
        stream.writePositiveInt(heroes["itemsAmount"], 7) # items amount (here its bounty stars)
        stream.writePositiveInt(heroes["unknown5"], 13) #idk
        stream.writePositiveInt(heroes["unknown6"], 11) # idk
        stream.writeBoolean(heroes["unknown7"]) # idk
        stream.writeBoolean(heroes["hasImmunityShield"]) # is immune
        stream.writeBoolean(heroes["rotationRelated2"]) # rotate related
        stream.writeBoolean(heroes["hasRage"]) # dev rage activated
        stream.writeBoolean(heroes["ultiAiming"])# aiming with ulti
        stream.writeBoolean(heroes["activedUlti"]) # ulti activated
        stream.writeBoolean(heroes["invisible"]) # invisible
        stream.writeBoolean(heroes["notFullyVisible"])  # not fully visible
        stream.writePositiveInt(heroes["unknown8"], 9) # idk
        if index == 1:
            stream.writeBoolean(heroes["unknown9"]) # idk but its only for your player
            stream.writePositiveInt(heroes["unknown10"], 9) # same
        stream.writePositiveInt(len(heroes["damagesArray"]), 5) # damages count
        for index, x in heroes["damagesArray"].items():
            stream.writeBoolean(heroes["damagesArray"][index]["unknown"]) # why not.....
            stream.writePositiveInt(heroes["damagesArray"][index]["damage"], 12) # damages dealt
        # skills array
        # skills
        for name, x in heroes["skillsArray"].items():
            stream.writePositiveInt(heroes["skillsArray"][name]["activeTicks"], 11) # active ticks
            stream.writeBoolean(heroes["skillsArray"][name]["unknown"]) #is active i think
            stream.writePositiveInt(heroes["skillsArray"][name]["unknown1"], 12) # unk
            if name == "Weapon":
                stream.writePositiveInt(heroes["skillsArray"][name]["ammos"], 12) # your ammos 1000 = 1 full ammo (only if max charge is higher then 0)

