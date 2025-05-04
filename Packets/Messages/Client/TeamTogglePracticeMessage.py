from Packets.Messages.Server.TeamMessage import TeamMessage
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase

class TeamTogglePractiseMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        pass
        

    def process(self):
        db = DataBase(self.player)
        gamerooomInfo = db.getGameroomInfo("info")
        gamerooomInfo["practice"] = not gamerooomInfo["practice"]
        db.updateGameroomInfo(gamerooomInfo["practice"], self.player.teamID, "practice")
        gameroomInfo = db.getGameroomInfo("info")
        for player_key, values in gameroomInfo["players"].items():
            TeamMessage(self.device, self.player).SendTo(player_key)