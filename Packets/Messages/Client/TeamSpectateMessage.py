from Packets.Messages.Server.TeamMessage import TeamMessage
from Logic.Player import Player
from Utils.Reader import ByteStream
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.TeamErrorMessage import TeamErrorMessage

class TeamSpectateMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        self.fields = {}
        self.fields["Unk1"] = self.readVInt()
        self.fields["Unk2"] = self.readVInt()
        self.fields["Unk3"] = self.readVInt()

    def process(self):
        if self.player.teamID != 0:
            return "nuh uh"
        db = DataBase(self.player)
        #try:
        joined = db.joinGameroom(self.fields["Unk2"])
        if joined:
            db.connection.commit()
            self.player.teamID = self.fields["Unk2"]
            db.replaceValue('teamID', self.player.teamID)
            db.addGameroomMsg(self.player.teamID, 4, self.player.low_id, self.player.name, " ", 102, self.player.low_id, self.player.name)
            gameroomInfo = db.getGameroomInfo("info")
            for player_key, values in gameroomInfo["players"].items():
                TeamMessage(self.device, self.player).SendTo(player_key)
        else:
            TeamErrorMessage(self.device, self.player, 6).Send()