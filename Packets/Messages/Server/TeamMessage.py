from Utils.Writer import Writer
from Files.CsvLogic.Cards import Cards
from Database.DatabaseManager import DataBase

class TeamMessage(Writer):
    def __init__(self, device, player):
        self.id = 24124
        self.device = device
        self.player = player
        super().__init__(self.device)


    def encode(self):
            db = DataBase(self.player)
            gameroomInfo = db.getGameroomInfo("info")
            self.writeVInt(gameroomInfo["room_type"])  # Game Room Type
            self.writeBoolean(gameroomInfo["practice"]) # Practice With Bots
            self.writeVInt(3) # Game Room Maximun Players
            self.writeLong(0, self.player.teamID)
            self.writeVInt(1) # Unk, is this a timestamp
            self.writeVLong(gameroomInfo["advertisedClub"][0], gameroomInfo["advertisedClub"][1])
            self.writeScID(15, gameroomInfo["map_id"]) # Location ID
            self.playerCount = gameroomInfo["player_count"]
            self.writeVint(self.playerCount)
            for player, values in gameroomInfo["players"].items():
                playerToken = db.getTokenByLowId(gameroomInfo["players"][player]["low_id"])
                playersData = (db.getSpecifiedPlayers([playerToken]))[0]
                self.writeLong(0, gameroomInfo["players"][player]["low_id"]) # Player ID
                
                self.writeString(gameroomInfo["players"][player]["name"]) # Player Name
                self.writeVInt(69) # Player Experience Level (unused)
                self.writeScID(16, gameroomInfo["players"][player]["brawler_id"]) # Player Brawler
                self.writeScID(0, 1) # Player Skin
                brawler_id = str(gameroomInfo["players"][player]["brawler_id"])
                self.writeVInt(playersData["unlocked_brawlers"][brawler_id]["Trophies"]) # Brawler Trophies
                self.writeVInt(playersData["unlocked_brawlers"][brawler_id]["HighestTrophies"]) # Brawler Trophies for Rank
                powerLevel = 0
                for card, amount in playersData["unlocked_brawlers"][brawler_id]["Cards"].items():
                    if not Cards().isUnlock(card):
                        powerLevel += amount
                self.writeVInt(powerLevel-1)
                self.writeVInt(gameroomInfo["players"][player]["status"] if playersData["player_status"] != 0 else 0) # Player Status
                self.writeVInt(1) # unk
                self.writeBoolean(gameroomInfo["players"][player]["ready"]) # Ready State
                self.writeVInt(gameroomInfo["players"][player]["team"]) # Player Team
            # Players Array End