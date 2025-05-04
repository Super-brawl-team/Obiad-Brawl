from Packets.Messages.Server.MyAlliance import MyAlliance
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase
import time
from Packets.Messages.Server.AllianceEventMessage import AllianceEventMessage
from Packets.Messages.Server.AllianceChatServer import AllianceChatServer
class AllianceEditSettings(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player
        self.HighID = 0
        self.LowID = 0

    def decode(self):
        self.desc = self.readString()
        self.badge = self.readDataReference()
        self.type = self.readVInt()
        self.trophiesRequired = self.readVInt()

    def process(self):
        db = DataBase(self.player)
        if self.player.club_id == 0:
            return "nop"
        if self.player.club_role in [0, 1]:
            return "nop"
        db.replaceClubValue(self.player.club_id, self.desc, self.badge[1], self.type, self.trophiesRequired)
        AllianceEventMessage(self.device, self.player, 10).Send()
        club =  db.loadClub(self.player.club_id)
        self.plrids = []
        for token in club["info"]["memberCount"]:
            memberData = db.getMemberData(token)
            self.plrids.append(memberData["low_id"])
        for id in self.plrids:
            if id != self.targetID[1]:
                MyAlliance(self.device, self.player).SendTo(id)
        