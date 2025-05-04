from Packets.Messages.Server.TeamMessage import TeamMessage
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase

class TeamChangeMemberSettingsMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        self.readVInt()
        self.player.selectedCard = self.readDataReference()


    def process(self):
       db = DataBase(self.player)
       playerInfo = db.getPlayerInfo(self.player.low_id)
       playerInfo["brawler_id"] = self.player.selectedCard[1]
       db.updateGameroomPlayerInfo(self.player.low_id, self.player.teamID, playerInfo)
       gameroomInfo = db.getGameroomInfo("info")
       for player_key, values in gameroomInfo["players"].items():
            TeamMessage(self.device, self.player).SendTo(player_key)
       