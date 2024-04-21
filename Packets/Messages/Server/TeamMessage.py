from Utils.Writer import Writer
import random


class TeamMessage(Writer):
    def __init__(self, device, player):
        self.id = 24124
        self.device = device
        self.player = player
        self.playerCount = 3
        self.names = [self.player.name, "Bot 1", "Bot 2"]
        super().__init__(self.device)


    def encode(self):
            
        if self.player.teamID != 0:
            self.writeVInt(self.player.teamType) # Game Room Type
            self.writeBoolean(self.player.isTeamInPracticeMode) # Practice With Bots
            self.writeVInt(3) # Game Room Maximun Players
            self.writeLong(0, self.player.teamID) # Room Code
            self.writeVInt(0) # Unk, is this a timestamp
            self.writeBoolean(self.player.isAdvertiseToBand) # Advertise to Band
            self.writeBoolean(self.player.isAdvertiseToBand) # Advertise to Band
            self.writeScID(15, 0) # Location ID


            # Players Array
            self.writeVInt(self.playerCount) # Players Count
            for player in range(self.playerCount):
                
                if player == 0:
                    self.writeLong(0, 1) # Player ID
                else:
                    self.writeLong(0, random.randint(2, 2147483647))
                self.writeString(self.names[player]) # Player Name
                self.writeVInt(69) # Player Experience Level (unused)
                self.writeScID(self.player.selectedCard[0], self.player.selectedCard[1]) # Player Brawler
                self.writeScID(29, 0) # Player Skin
                self.writeVInt(500) # Brawler Trophies
                self.writeVInt(500) # Brawler Trophies for Rank
                self.writeVInt(15) # Brawler Upgrade Level
                self.writeVInt(self.player.teamStatus) # Player Status
                self.writeVInt(0) # unk
                self.writeBoolean(self.player.TeamReadyState) # Ready State
                self.writeVInt(player + 1) # Player Team
            # Players Array End