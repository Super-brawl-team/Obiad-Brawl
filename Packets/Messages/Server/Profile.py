# -*- coding: utf-8 -*-
from Utils.Writer import Writer
<<<<<<< Updated upstream


=======
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters
import json
from Database.DatabaseManager import DataBase
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
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
=======
        db = DataBase(self.player)
        for player in self.players:
            if self.LowID == player["low_id"]:
                self.writeVInt(self.HighID) # Player HighID
                self.writeVInt(self.LowID) # Player LowID
                self.writeString(player["name"])
                self.writeVInt(0) # Unknown Data 
                
                self.writeVInt(len(player["unlocked_brawlers"])) 
                
                
                # Hero Entry Array
                for key, brawler_id in player["unlocked_brawlers"].items():
                    self.writeScId(16, int(key))
                    self.writeVInt(0)
                    self.writeVInt(brawler_id["Trophies"])  # Trophies 
                    self.writeVInt(brawler_id["HighestTrophies"])  # Trophies for rank
                    powerLevel = 0
                    for card, amount in brawler_id["Cards"]:
                        if not Cards().isUnlock(card):
                            powerLevel += amount
                    self.writeVInt(powerLevel) # Brawler Upgrade Level TOO
>>>>>>> Stashed changes
                # Hero Entry Array End
                
                
                # Stats Entry Array
<<<<<<< Updated upstream
                self.writeVint(7) # Stats Count
                self.writeVint(1) # Stats Index
                self.writeVint(666) # Total Victories
=======
                self.writeVInt(7) # Stats Count
                self.writeVInt(1) # Stats Index
                self.writeVInt(player["three_vs_three_wins"]) # Total Victories
>>>>>>> Stashed changes
                self.writeVint(2) # Stats Index
                self.writeVint(player["player_experience"]) # Player Experience Points
                self.writeVint(3) # Stats Index
<<<<<<< Updated upstream
                self.writeVint(2000) # Player Trophies
                self.writeVint(4) # Stats Index
                self.writeVint(2000) # Highest Trophies
                self.writeVint(5) # Stats Index
                self.writeVint(15) # Unlocked Brawlers
                self.writeVint(7) # Stats Index
                self.writeVint(28000000 + 1) # Player Profile Icon
                self.writeVint(8) # Stats Index
                self.writeVint(1488) # Showdown Victories
=======
                self.writeVint(player["trophies"]) # Player Trophies
                self.writeVint(4) # Stats Index
                self.writeVint(player["highest_trophies"]) # Highest Trophies
                self.writeVint(5) # Stats Index
                self.writeVint(len(player["unlocked_brawlers"])) # Unlocked Brawlers
                self.writeVint(7) # Stats Index
                self.writeVint(28000000 + player["profile_icon"]) # Player Profile Icon
                self.writeVint(8) # Stats Index
                self.writeVint(player["solo_wins"]) # Showdown Victories
>>>>>>> Stashed changes
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