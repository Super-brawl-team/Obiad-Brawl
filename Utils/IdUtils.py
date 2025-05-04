# -*- coding: utf-8 -*-
import math
class IdUtils:
    def __init__(self):
        self.TagChar = ("0", "2", "8", "9", "P", "Y", "L", "Q", "G", "R", "J", "C", "U", "V")
        
    def getId(self, Hashtag):
        if not Hashtag.startswith('#'):
            return 0
        TagArray = list(Hashtag[1:].upper())
        Id = 0
        for i in range(len(TagArray)):
            Character = TagArray[i]
            try:
                CharIndex = self.TagChar.index(Character)
            except ValueError:
                return 0
            Id *= len(self.TagChar)
            Id += CharIndex
        return Id
    
    def getHLId(self, Hashtag):
        if not Hashtag.startswith('#'):
            return [0, 0]
        TagArray = list(Hashtag[1:].upper())
        Id = 0
        for i in range(len(TagArray)):
            Character = TagArray[i]
            try:
                CharIndex = self.TagChar.index(Character)
            except ValueError:
                return [0, 0]
            Id *= len(self.TagChar)
            Id += CharIndex
        HighLow = []
        HighLow.append(Id % 256)
        HighLow.append((Id - HighLow[0]) >> 8)
        return HighLow
    
 

    def getIdFromHl(self):
        High = int(input('>>'))
        Low = int(input('>>'))
        return (Low << 8) + High


    def getHashtagfromId(self, Id = None):
        if not Id:
            Id = self.getIdFromHl()
        Tag = []
        while Id > 0:
            CharIndex = math.floor(Id % len(self.TagChar))
            Tag.insert(0,self.TagChar[CharIndex])
            Id -= CharIndex
            Id /= len(self.TagChar)

        return ''.join(Tag)