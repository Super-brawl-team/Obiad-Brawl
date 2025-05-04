from Packets.Messages.Server.TeamLeftMessage import TeamLeftMessage
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.TeamChatServerMessage import TeamStreamMessage
from Packets.Messages.Server.TeamMessage import TeamMessage

class TeamKickMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        self.targetID = self.readLogicLong()

    def process(self):
        if self.player.teamID == 0:
            return "kek"
        
        db = DataBase(self.player)
        gameroomInfo = db.getGameroomInfo("info")
        TeamLeftMessage(self.device, self.player, 1).SendTo(self.targetID[1])
        playerToken = db.getTokenByLowId(self.targetID[1])
        db.removeGameroomPlayer(self.targetID[1], self.player.teamID, playerToken)
        db.addGameroomMsg(self.player.teamID, 4, self.player.low_id, self.player.name, "", 104, self.targetID[1], self.player.name)
        tick = db.getNextGameroomKey(self.player.teamID)
        db.loadGameroom()
        for player_key, values in gameroomInfo["players"].items():
            if player_key != self.targetID[1]:
                TeamStreamMessage(self.device, self.player, tick).SendTo(player_key)
                TeamMessage(self.device, self.player).SendTo(player_key)
        

        db.replaceOtherValue("teamID", 0, playerToken)
        