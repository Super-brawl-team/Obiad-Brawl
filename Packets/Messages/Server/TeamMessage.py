from Utils.Writer import Writer
import random
import json
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters

class TeamMessage(Writer):
    def __init__(self, device, player):
        self.id = 24124
        self.device = device
        self.player = player
        self.playerCount = 3
        self.names = [self.player.name, "Bot 1", "Bot 2"]
        super().__init__(self.device)


    def encode(self):
            Brawlers228 = Cards().getBrawlers()
            self.settings = json.load(open('Settings.json'))
            self.maximumRank = self.settings["MaximumRank"]
            self.maximumUpgradeLevel = self.settings["MaximumUpgradeLevel"]
            self.requiredTrophiesForRank = ProgressStart = [0,10,20,30,40,60,80,100,120,140,160,180,220,260,300,340,380,420,460,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200]
            if self.maximumRank <= 34:
                      self.brawlersTrophies = self.requiredTrophiesForRank[self.maximumRank-1]
            else:
                      self.brawlersTrophies = self.brawlersTrophies = self.requiredTrophiesForRank[33] + (50* (self.maximumRank-34))
            self.writeVInt(0) # Game Room Type
            self.writeBoolean(self.player.isTeamInPracticeMode) # Practice With Bots
            self.writeVInt(3) # Game Room Maximun Players
            self.writeLong(0, self.player.teamID)
            self.writeVInt(0) # Unk, is this a timestamp
            self.writeVInt(0) # Advertise to Band?
            self.writeVInt(0) # Advertise to Band?
            self.writeScID(15, 0) # Location ID


            # Players Array
            self.writeVInt(self.playerCount) # Players Count
            for player in range(self.playerCount):
                
                if player == 0:
                    self.writeLong(0, 1) # Player ID
                else:
                    self.writeLong(1, player)
                self.writeString(self.names[player]) # Player Name
                self.writeVInt(69) # Player Experience Level (unused)
                self.writeScID(self.player.selectedCard[0], self.player.selectedCard[1]) # Player Brawler
                self.writeScID(29, 1) # Player Skin
                self.writeVInt(self.brawlersTrophies) # Brawler Trophies
                self.writeVInt(self.brawlersTrophies) # Brawler Trophies for Rank
                self.writeVInt(self.maximumUpgradeLevel*3) # Brawler Upgrade Level
                self.writeVInt(self.player.teamStatus) # Player Status
                self.writeVInt(0) # unk
                self.writeBoolean(self.player.isReadyState) # Ready State
                self.writeVInt(player) # Player Team
            # Players Array End