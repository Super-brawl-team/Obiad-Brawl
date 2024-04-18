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
            
        if self.player.room_id != 0:
            self.writeVInt(0) # Game Room Type
            self.writeBoolean(True) # Practice With Bots
            self.writeVInt(3) # Game Room Maximun Players
            self.writeLong(0, self.player.teamID) # Room Code
            self.writeVint(1557129593) # Unk, is this a timestamp
            self.writeBoolean(False) # Adversitise to Band
            self.writeVInt(1) # Event Slot Index
            self.writeVInt(1) # Event Slot Index
            self.writeScID(15, 0) # Location ID


            # Players Array
            self.writeVint(self.playerCount) # Players Count
            for player in range(self.playerCount):
                self.writeVInt(1) # Game Room Owner State
                if player == 0:
                    self.writeLong(0, 1) # Player ID
                else:
                    self.writeLong(0, random.randint(2, 2147483647))
                self.writeString(self.names[player]) # Player Name
                self.writeVInt(0) # Player Experience Level (unused)
                self.writeScID(16, 0) # Player Brawler
                self.writeScID(29, 0) # Player Skin
                self.writeVInt(500) # Brawler Trophies
                self.writeVInt(500) # Brawler Trophies for Rank
                self.writeVInt(5) # Brawler Upgrade Level
                self.writeVInt(self.player.teamStatus) # Player Status
                self.writeBoolean(self.player.TeamReadyState) # Ready State
                self.writeVInt(player) # Player Team
            # Players Array End