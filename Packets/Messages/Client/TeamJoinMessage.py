from Packets.Messages.Server.TeamMessage import TeamMessage
from Utils.Reader import ByteStream
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.TeamErrorMessage import TeamErrorMessage
from Packets.Messages.Server.TeamChatServerMessage import TeamStreamMessage as TeamChatServerMessage
from Packets.Messages.Server.TeamStreamMessage import TeamStreamMessage

class TeamJoinMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        self.fields["Unk1"] = self.readVInt()
        self.fields["Unk2"] = self.readVInt()
        self.fields["Unk3"] = self.readVInt()
        super().decode(self.fields)
        return self.fields

    def process(self):
        if self.player.teamID != 0:
            return "nuh uh"
        db = DataBase(self.player)
        joined = db.joinGameroom(self.fields["Unk2"])
        if joined:
            db.connection.commit()
            self.player.teamID = self.fields["Unk2"]
            db.replaceValue('room_id', self.player.teamID)
            TeamMessage(self.device, self.player).Send()
            TeamStreamMessage(self.device, self.player).Send()
            db.addGameroomMsg(self.player.teamID, 4, self.player.low_id, self.player.name, " ", 102, self.player.low_id, self.player.name)
            gameroomInfo = db.getGameroomInfo("info")
            tick = db.getNextGameroomKey(self.player.teamID)
            for player_key, values in gameroomInfo["players"].items():
                TeamChatServerMessage(self.device, self.player, tick).SendTo(player_key)
                TeamMessage(self.device, self.player).SendTo(player_key)
        else:
            TeamErrorMessage(self.device, self.player, 6)