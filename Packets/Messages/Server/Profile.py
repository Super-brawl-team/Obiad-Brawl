# -*- coding: utf-8 -*-
from Utils.Writer import Writer


class Profile(Writer):

    def __init__(self, device, player, HighID, LowID, players):
        self.id = 24113
        self.device = device
        self.player = player
        self.HighID = HighID
        self.LowID = LowID
        self.players = players
        super().__init__(self.device)

    def encode(self):
                self.writeVint(self.HighID) # Player HighID
                self.writeVint(self.LowID) # Player LowID
                self.writeString("<cee1200>P<ce85400>r<ce19700>i<cdada00>m<cdada00>o<c92e507>D<c49f00e>E<c00fc16>V<c00fc16>H<c16a862>a<c2c54ae>c<c4200fa>c</c>")
                self.writeVint(0) # Unknown Data 
                
                self.writeVint(15) 
                
                
                # Hero Entry Array
                for x in range(15):
                    self.writeScId(16, x)
                    self.writeVint(0)
                    self.writeVint(999)  # Trophies 
                    self.writeVint(999)  # Trophies for rank
                    self.writeVint(15) # Brawler Upgrade Level
                # Hero Entry Array End
                
                
                # Stats Entry Array
                self.writeVint(7) # Stats Count
                self.writeVint(1) # Stats Index
                self.writeVint(666) # Total Victories
                self.writeVint(2) # Stats Index
                self.writeVint(666) # Player Experience Points
                self.writeVint(3) # Stats Index
                self.writeVint(2000) # Player Trophies
                self.writeVint(4) # Stats Index
                self.writeVint(2000) # Highest Trophies
                self.writeVint(5) # Stats Index
                self.writeVint(15) # Unlocked Brawlers
                self.writeVint(7) # Stats Index
                self.writeVint(28000000 + 1) # Player Profile Icon
                self.writeVint(8) # Stats Index
                self.writeVint(1488) # Showdown Victories
                # Stats Entry Array End
                # Player Profile End
                

                # Alliance Header Entry Array
                
                self.writeBool(True) # Joined in a Band
                self.writeInt(0) # Band HighID
                self.writeInt(1) # Band LowID
                self.writeString("Primo Team") # Band Name
                self.writeScId(8, 19) # Band Badge
                self.writeVint(1) # Band Type
                self.writeVint(1) # Band Members
                self.writeVint(0) # Band Trophies
                self.writeVint(0) # Band Required Trophies
                self.writeScId(14, 249) # Unknown Data Reference
                self.writeScID(25, 2) # Unknown