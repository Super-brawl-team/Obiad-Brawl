# -*- coding: utf-8 -*-
from Utils.Writer import Writer

from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters
import json
from Database.DatabaseManager import DataBase
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

        db = DataBase(self.player)
        for player in self.players:
            if self.LowID == player["low_id"]:
                self.writeVInt(self.HighID) # Player HighID
                self.writeVInt(self.LowID) # Player LowID
                self.writeString(player["name"])
                self.writeVInt(0) # Unknown Data 
                
                self.writeVInt(len(player["unlocked_brawlers"])) 

                for key, brawler_id in player["unlocked_brawlers"].items():
                    self.writeScId(16, int(key))
                    self.writeVInt(0)
                    self.writeVInt(brawler_id["Trophies"])  # Trophies 
                    self.writeVInt(brawler_id["HighestTrophies"])  # Trophies for rank
                    powerLevel = 0
                    for card, amount in brawler_id["Cards"].items():
                        if not Cards().isUnlock(card):
                            powerLevel += amount
                    self.writeVInt(powerLevel) # Brawler Upgrade Level TOO

                self.writeVInt(7) # Stats Count
                self.writeVInt(1) # Stats Index
                self.writeVInt(player["three_vs_three_wins"]) # Total Victories

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