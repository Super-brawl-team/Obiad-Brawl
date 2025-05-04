from Packets.Messages.Server.TeamMessage import TeamMessage
from Logic.Player import Player
from Utils.Reader import ByteStream
from Database.DatabaseManager import DataBase

class TeamMemberStatusMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        self.player.teamStatus = self.readVInt()
        


    def process(self):
       db = DataBase(self.player)
       playerInfo = db.getPlayerInfo(self.player.low_id)
       playerInfo['status'] = self.player.teamStatus
       db.updateGameroomPlayerInfo(self.player.low_id, self.player.teamID, playerInfo)
       gameroomInfo = db.getGameroomInfo("info")
       for player_key, values in gameroomInfo["players"].items():
            TeamMessage(self.device, self.player).SendTo(player_key)
       