from Packets.Messages.Server.MyAlliance import MyAlliance
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase
import time
from Packets.Messages.Server.AllianceEventMessage import AllianceEventMessage
from Packets.Messages.Server.ClanStream import ClanStream
class AllianceCreate(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player
        self.HighID = 0
        self.LowID = 0

    def decode(self):
        self.club_name = self.readString()
        self.desc = self.readString()
        self.badge = self.readDataReference()
        self.type = self.readVInt()
        self.trophiesRequired = self.readVInt()

    def process(self):
        db = DataBase(self.player)
        if self.player.club_id != 0:
            return "nop"
        db.getClubId()
        db.replaceValue('club_id', self.player.club_id)
        db.replaceValue('club_role', 2)
        self.player.club_role = 2

        # Club creation
        db.createClub(self.player.club_id, {"info": {"clubID": self.player.club_id, "name": self.club_name, "description": self.desc, "region": self.player.region, "clubBadge": self.badge[1], "clubType": self.type, "requiredTrophies": self.trophiesRequired, "trophies": self.player.trophies, "memberCount": [self.player.token], "onlineMembers": 1}}, {"info": {"clubID": self.player.club_id, "messages": { "0": {"EventType": 4, "Event": 3, "Tick": 0, "PlayerID": self.player.low_id, "PlayerName": self.player.name, "PlayerRole": self.player.club_role, "Message": "", "promotedTeam": 0, "TimeStamp": time.time(), "targetID": self.player.low_id, "targetName": self.player.name}}}})
        AllianceEventMessage(self.device, self.player, 20).Send()
        MyAlliance(self.device, self.player).Send() # 14109
        ClanStream(self.device, self.player).Send()