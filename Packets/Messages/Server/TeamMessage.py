from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class TeamMessage(Writer):
    def __init__(self, device, player):
        self.id = 24124
        self.device = device
        self.player = player
        self.playerCount = 3
        super().__init__(self.device)


    def encode(self):
            
        if self.player.room_id != 0:
            self.writeVInt(0) # Game Room Type
            self.writeBoolean(False) # Practice With Bots
            self.writeVInt(1) # Game Room Maximun Players
            self.writeLong(0, 1) # Room Code
            self.writeVint(1557129593) # Unk
            self.writeBoolean(False) # Adversitise to Band
            self.writeVInt(1) # Event Slot Index
            self.writeVInt(1) # Event Slot Index
            self.writeScID(15, 7) # Location ID


            # Players Array
            self.writeVint(self.playerCount) # Players Count
            for player in range(self.playerCount):
                self.writeVInt(1) # Game Room Owner State
                self.writeLong(0, 1) # Player ID
                self.writeString(self.player.name) # Player Name
                self.writeVInt(0) # Player Experience Level (unused)
                self.writeScID(16, 0) # Player Brawler
                self.writeScID(29, 0) # Player Skin
                self.writeVInt(500) # Brawler Trophies
                self.writeVInt(500) # Brawler Trophies for Rank
                self.writeVInt(5) # Brawler Upgrade Level
                self.writeVInt(3) # Player Status
                self.writeBoolean(False) # Ready State
                self.writeVInt(player) # Player Team
            # Players Array End