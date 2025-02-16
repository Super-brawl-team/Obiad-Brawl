from Packets.Messages.Server.MyAlliance import MyAlliance
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase
import time
from Packets.Messages.Server.AllianceEventMessage import AllianceEventMessage
from Packets.Messages.Server.AllianceChatServer import AllianceChatServer
class AllianceChat(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player
        self.HighID = 0
        self.LowID = 0

    def decode(self):
        self.msg = self.readString()
    
    def process(self):
        db = DataBase(self.player)
        db.addMsg(self.player.club_id, 2, self.player.low_id, self.player.name, self.player.club_role, self.msg, 0)
        db.loadClub(self.player.club_id)
        self.plrids = []
        club =  db.loadClub(self.player.club_id)
        nextKey = db.getNextKey(self.player.club_id)
        for token in club["info"]["memberCount"]:
            memberData = db.getMemberData(token)
            self.plrids.append(memberData["low_id"])
        for i in self.plrids:
            AllianceChatServer(self.device, self.player, self.player.club_id, nextKey+1).SendTo(i)