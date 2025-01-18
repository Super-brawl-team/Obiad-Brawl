# -*- coding: utf-8 -*-
from Utils.Writer import Writer
<<<<<<< Updated upstream
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters
import json

=======
<<<<<<< HEAD

from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters
import json
from Database.DatabaseManager import DataBase
=======
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters
import json

>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
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
                Brawlers228 = Characters().getBrawlers()
                cards = Cards().getCards()
                self.settings = json.load(open('Settings.json'))
                self.maximumRank = self.settings["MaximumRank"]
                self.maximumUpgradeLevel = self.settings["MaximumUpgradeLevel"]
                self.requiredTrophiesForRank = ProgressStart = [0,10,20,30,40,60,80,100,120,140,160,180,220,260,300,340,380,420,460,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200]
                if self.maximumRank <= 34:
                      self.brawlersTrophies = self.requiredTrophiesForRank[self.maximumRank-1]
                else:
                      self.brawlersTrophies = self.brawlersTrophies = self.requiredTrophiesForRank[33] + (50* (self.maximumRank-34))
=======
<<<<<<< HEAD

        db = DataBase(self.player)
        for player in self.players:
            if self.LowID == player["low_id"]:
>>>>>>> Stashed changes
                self.writeVInt(self.HighID) # Player HighID
                self.writeVInt(self.LowID) # Player LowID
                self.writeString(self.player.name)
                self.writeVInt(0) # Unknown Data 
                
                self.writeVInt(len(Brawlers228)) 
                
                
                # Hero Entry Array
                for x in Brawlers228:
                    self.writeScId(16, x)
                    self.writeVInt(0)
                    self.writeVInt(self.brawlersTrophies)  # Trophies 
                    self.writeVInt(self.brawlersTrophies)  # Trophies for rank
                    self.writeVInt(self.maximumUpgradeLevel*3) # Brawler Upgrade Level
                # Hero Entry Array End
                
                
                # Stats Entry Array
                self.writeVInt(7) # Stats Count
                self.writeVInt(1) # Stats Index
<<<<<<< Updated upstream
                self.writeVInt(666) # Total Victories
=======
                self.writeVInt(player["three_vs_three_wins"]) # Total Victories

=======
                Brawlers228 = Characters().getBrawlers()
                cards = Cards().getCards()
                self.settings = json.load(open('Settings.json'))
                self.maximumRank = self.settings["MaximumRank"]
                self.maximumUpgradeLevel = self.settings["MaximumUpgradeLevel"]
                self.requiredTrophiesForRank = ProgressStart = [0,10,20,30,40,60,80,100,120,140,160,180,220,260,300,340,380,420,460,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200]
                if self.maximumRank <= 34:
                      self.brawlersTrophies = self.requiredTrophiesForRank[self.maximumRank-1]
                else:
                      self.brawlersTrophies = self.brawlersTrophies = self.requiredTrophiesForRank[33] + (50* (self.maximumRank-34))
                self.writeVInt(self.HighID) # Player HighID
                self.writeVInt(self.LowID) # Player LowID
                self.writeString(self.player.name)
                self.writeVInt(0) # Unknown Data 
                
                self.writeVInt(len(Brawlers228)) 
                
                
                # Hero Entry Array
                for x in Brawlers228:
                    self.writeScId(16, x)
                    self.writeVInt(0)
                    self.writeVInt(self.brawlersTrophies)  # Trophies 
                    self.writeVInt(self.brawlersTrophies)  # Trophies for rank
                    self.writeVInt(self.maximumUpgradeLevel*3) # Brawler Upgrade Level
                # Hero Entry Array End
                
                
                # Stats Entry Array
                self.writeVInt(7) # Stats Count
                self.writeVInt(1) # Stats Index
                self.writeVInt(666) # Total Victories
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
                self.writeVint(2) # Stats Index
                self.writeVint(666) # Player Experience Points
                self.writeVint(3) # Stats Index
<<<<<<< Updated upstream
                self.writeVint(self.brawlersTrophies* len(Brawlers228)) # Player Trophies
=======
<<<<<<< HEAD

                self.writeVint(player["trophies"]) # Player Trophies
>>>>>>> Stashed changes
                self.writeVint(4) # Stats Index
                self.writeVint(self.brawlersTrophies* len(Brawlers228)) # Highest Trophies
                self.writeVint(5) # Stats Index
                self.writeVint(len(Brawlers228)) # Unlocked Brawlers
                self.writeVint(7) # Stats Index
                self.writeVint(28000000 + 0) # Player Profile Icon
                self.writeVint(8) # Stats Index
<<<<<<< Updated upstream
                self.writeVint(6969) # Showdown Victories
=======
                self.writeVint(player["solo_wins"]) # Showdown Victories

                self.writeVint(2) # Stats Index
                self.writeVint(player["player_experience"]) # Player Experience Points
                self.writeVint(3) # Stats Index
                self.writeVint(player["trophies"]) # Player Trophies
                self.writeVint(4) # Stats Index
                self.writeVint(player["highest_trophies"]) # Highest Trophies
                self.writeVint(5) # Stats Index
                self.writeVint(len(player["unlocked_brawlers"])) # Unlocked Brawlers
                self.writeVint(7) # Stats Index
                self.writeVint(28000000 + player["profile_icon"]) # Player Profile Icon
                self.writeVint(8) # Stats Index
                self.writeVint(player["solo_wins"]) # Showdown Victories

=======
                self.writeVint(self.brawlersTrophies* len(Brawlers228)) # Player Trophies
                self.writeVint(4) # Stats Index
                self.writeVint(self.brawlersTrophies* len(Brawlers228)) # Highest Trophies
                self.writeVint(5) # Stats Index
                self.writeVint(len(Brawlers228)) # Unlocked Brawlers
                self.writeVint(7) # Stats Index
                self.writeVint(28000000 + 0) # Player Profile Icon
                self.writeVint(8) # Stats Index
                self.writeVint(6969) # Showdown Victories
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
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