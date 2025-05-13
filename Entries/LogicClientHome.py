from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
import json
from Entries.LogicDailyData import LogicDailyData
from Entries.LogicConfData import LogicConfData
class LogicClientHome:
    def encode(self: Writer, player):
        self.player = player
        LogicDailyData.encode(self, self.player)
        LogicConfData.encode(self, self.player)
        self.writeLong(self.player.high_id, self.player.low_id)  # Player id