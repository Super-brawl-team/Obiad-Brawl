from Packets.Messages.Server.MyAlliance import MyAlliance
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase
import time
from Packets.Messages.Server.AllianceEventMessage import AllianceEventMessage
from Packets.Messages.Server.AllianceChatServer import AllianceChatServer
class AllianceLeave(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player
        self.HighID = 0
        self.LowID = 0

    def decode(self):
        pass
    
    def process(self):
        db = DataBase(self.player)
        # Removing member 
        club =  db.loadClub(self.player.club_id)

        if len(club["info"]["memberCount"]) == 1:
            db.addMember(self.player.club_id, self.player.token, 0)

        else:
            db.addMember(self.player.club_id, self.player.token, 2)
            db.addMsg(self.player.club_id, 4, self.player.low_id, self.player.name, self.player.club_role, "", 4, self.player.low_id, self.player.name)
            self.plrids = []
            nextKey = db.getNextKey(self.player.club_id)
            for token in club["info"]["memberCount"]:
                memberData = db.getMemberData(token)
                self.plrids.append(memberData["low_id"])
            for low_id in self.plrids:
                AllianceChatServer(self.device, self.player, self.player.club_id, nextKey+1).SendTo(low_id)
                MyAlliance(self.device, self.player).SendTo(id)

        # Info
        self.player.club_id = 0
        db.replaceValue('club_id', self.player.club_id)
        self.player.club_id = 0
        db.replaceValue('club_role', 0)
        self.player.club_role = 0
        AllianceEventMessage(self.device, self.player, 80).Send()
        MyAlliance(self.device, self.player).Send()
        
        
        