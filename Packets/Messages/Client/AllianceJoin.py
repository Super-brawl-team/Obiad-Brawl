from Packets.Messages.Server.MyAlliance import MyAlliance
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase
import time
from Packets.Messages.Server.AllianceEventMessage import AllianceEventMessage
from Packets.Messages.Server.AllianceChatServer import AllianceChatServer
from Packets.Messages.Server.ClanStream import ClanStream
class AllianceJoin(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player
        self.HighID = 0
        self.LowID = 0

    def decode(self):
        self.player.club_high_id = self.readInt()
        self.player.club_id = self.readInt()
    def process(self):
        db = DataBase(self.player)
        self.player.club_role = 1
        db.replaceValue('club_role', 1)
        db.replaceValue('club_id', self.player.club_id)

        # Member adding
        db.addMember(self.player.club_id, self.player.token, 1)
        db.addMsg(self.player.club_id, 4, self.player.low_id, self.player.name, self.player.club_role, "", 3, self.player.low_id, self.player.name)

        # Info
        club =  db.loadClub(self.player.club_id)
        nextKey = db.getNextKey(self.player.club_id)
        #AllianceMemberEntryMessage(self.client, self.player).sendToOthers()
        AllianceEventMessage(self.device, self.player, 40).Send()
        MyAlliance(self.device, self.player).Send() # 14109
        ClanStream(self.device, self.player).Send()
        self.plrids = []
        for token in club["info"]["memberCount"]:
            memberData = db.getMemberData(token)
            self.plrids.append(memberData["low_id"])
        for low_id in self.plrids:
            AllianceChatServer(self.device, self.player, self.player.club_id, nextKey+1).SendTo(low_id)
            MyAlliance(self.device, self.player).SendTo(id)