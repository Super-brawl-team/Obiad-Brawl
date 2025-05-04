from Packets.Messages.Server.AllianceChatServer import AllianceChatServer
from Packets.Messages.Server.AllianceEventMessage import AllianceEventMessage
from Database.DatabaseManager import DataBase
from Packets.PiranhaMessage import PiranhaMessage

class RequestJoinAllianceMessage(PiranhaMessage):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.fields = {}
        self.fields["clubID"] = self.readLong()
        self.fields["promotionMessage"] = self.readString()

    def process(self):
        db = DataBase(self.player)
        db.addMsg(self.fields["clubID"][1], 3, self.player.low_id, self.player.name, self.player.club_role, self.fields["promotionMessage"], 1)
        self.plrids = []
        club =  db.loadClub(self.fields["clubID"][1])
        nextKey = db.getNextKey(self.fields["clubID"][1])
        for token in club["info"]["memberCount"]:
            memberData = db.getMemberData(token)
            self.plrids.append(memberData["low_id"])
        for id in self.plrids:
                AllianceChatServer(self.device, self.player,self.fields["clubID"][1], nextKey+1).SendTo(id)
        AllianceEventMessage(self.device, self.player, 50).Send()
        