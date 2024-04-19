from Utils.Writer import Writer
import random


class StartLoadingMessage(Writer):
    def __init__(self, device, player):
        self.id = 20559
        self.device = device
        self.player = player
        super().__init__(self.device)


    def encode(self):
        self.writeInt(6) # Game Mode Total Players
        self.writeInt(0)
        self.writeInt(0)


        #Logic Player Array
        self.writeInt(6) # Players Count
        for x in range(1):
             
             self.writeLong(0, 1)
             self.writeString(self.player.name) # Player name
             self.writeVInt(x) # Player Team
             self.writeVInt(0) # ???
             self.writeVInt(0) # ???
             self.writeVInt(0) # ???
             self.writeInt(0) # unk
             self.writeScId(16, 0) # Player Brawler
             self.writeScId(29, 0) # Player Skin
             self.writeInt(0) # an array hmmm
        for x in range(2):
             
             self.writeLong(0, random.randint(30, 300)) # friend bot id
             self.writeString("Bot") # Player name
             self.writeVint(x+1) # Player Team
             self.writeVint(0) # ???
             self.writeVint(0) # ???
             self.writeVInt(0) # ???
             self.writeInt(0) # unk
             self.writeScId(16, 0) # Player Brawler
             self.writeScId(29, 0) # Player Skin
             self.writeInt(0) # an array hmmm
        for x in range(3):
             
             self.writeLong(0, random.randint(30, 300)) # enemy bot id
             self.writeString("Bot") # Player name
             self.writeVint(3+x) # Player Team
             self.writeVint(1) # ???
             self.writeVint(0) # ???
             self.writeVInt(0) # ???
             self.writeInt(0) # unk
             self.writeScId(16, 0) # Player Brawler
             self.writeScId(29, 0) # Player Skin
             self.writeInt(0) # an array hmmm
             
        
        self.writeInt(0) # Array
        self.writeVInt(1) # unknown
        self.writeVint(1) # drawmap
        self.writeVint(0) # Map Blocks
        self.writeBoolean(False) # Is spectating

        self.writeScId(15, 1) # Location ID
        self.writeBoolean(False)