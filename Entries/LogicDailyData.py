from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
from datetime import datetime
from time import *
import json
class LogicDailyData:
    def encode(self: Writer, player):
        self.player = player
        db = DataBase(self.player)
        self.settings = json.load(open('Settings.json'))
        self.writeVInt(2017189) # Timestamp
        self.writeVInt(10) # Create new band timer

        self.writeVInt(self.player.trophies)  # Trophies
        self.writeVInt(self.player.highest_trophies)  # Highest Trophies
        self.writeVInt(self.player.player_experience)  # Experience
        self.writeScID(28, self.player.profile_icon)  # Player Icon
        self.writeVInt(7) # Played Game Modes Count
        for x in range(7): 
            self.writeVInt(x) # Played Game Mode
        non_zero_skins = []
        for brawler in self.player.unlocked_brawlers.values():
            if brawler["selectedSkin"] != 0:
                non_zero_skins.append(brawler["selectedSkin"])
        self.writeVInt(len(non_zero_skins))
        for skin in non_zero_skins:
            self.writeDataReference(29, skin)

        non_zero_skins = []
        for brawler in self.player.unlocked_brawlers.values():
            for skin in brawler["Skins"]:
                if skin != 0:
                    non_zero_skins.append(skin)
        self.writeVInt(len(non_zero_skins))
        for skin in non_zero_skins:
            self.writeDataReference(29, skin)

        self.writeBool(True) # is time required to create new Band
        self.writeVInt(0) # unknown bruh
        self.writeVInt(self.player.coins_reward) # coins got
        self.writeVInt(self.player.control_mode) # Control Mode [0 - Tap to move, 1 - Joystick move, 2 - Double Joysticks (prototype)]
        self.writeBool(self.player.has_battle_hints) # is battle hints enabled
        self.writeVInt(self.player.coinsdoubler) # coins doubler coins remaining (0 = not activated)
        if self.player.coinsbooster - int(datetime.timestamp(datetime.now())) > 0:
            self.writeVInt(self.player.coinsbooster - int(datetime.timestamp(datetime.now()))) # coin boost secs remaining (0 = not activated)
        else:
            self.writeVInt(0)
            self.player.coinsbooster = int(datetime.timestamp(datetime.now()))
            db.replaceValue("coinsbooster", self.player.coinsbooster)
        self.writeBool(False) # unknown