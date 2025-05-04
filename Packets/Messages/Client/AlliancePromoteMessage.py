from Packets.Messages.Server.MyAlliance import MyAlliance
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase
import time
from Packets.Messages.Server.AllianceEventMessage import AllianceEventMessage
from Packets.Messages.Server.AllianceChatServer import AllianceChatServer
class AlliancePromoteMessage(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player
        self.HighID = 0
        self.LowID = 0

    def decode(self):
        self.targetID = self.readLong()
        self.TargetedRole = self.readVInt()
    
    def process(self):
        db = DataBase(self.player)
        if self.TargetedRole not in [0, 1, 2, 3, 4]:
            return "kek"
        if self.player.club_role not in [2, 4]:
            return "kek"
        if self.player.club_role == 3 and self.TargetedRole == (4 or 2) or self.player.club_role == 4 and self.TargetedRole == 2:
            return "kek"
        # Replacing value
        playertoken = db.getTokenByLowId(self.targetID[1])
        playersData = db.getSpecifiedPlayers([playertoken])
        playerData = playersData[0]
        db.replaceOtherValue('club_role', self.TargetedRole, playertoken)
        db.addMsg(self.player.club_id, 4, self.player.low_id, self.player.name, 0, "", 5, self.targetID[1], playerData["name"])
        self.plrids = []
        club =  db.loadClub(self.player.club_id)
        nextKey = db.getNextKey(self.player.club_id)
        for token in club["info"]["memberCount"]:
            memberData = db.getMemberData(token)
            self.plrids.append(memberData["low_id"])
        for id in self.plrids:
                AllianceChatServer(self.device, self.player, self.player.club_id, nextKey+1).SendTo(id)
        if self.TargetedRole == 2:
            self.player.club_role = 4
            db.replaceValue("club_role", self.player.club_role)
            db.addMsg(self.player.club_id, 4, self.player.low_id, self.player.name, 0, "", 6, self.player.low_id, self.player.name)
            self.plrids = []
            nextKey = db.getNextKey(self.player.club_id)
            for token in club["info"]["memberCount"]:
                memberData = db.getMemberData(token)
                self.plrids.append(memberData["low_id"])
            for id in self.plrids:
                    AllianceChatServer(self.device, self.player, self.player.club_id, nextKey+1).SendTo(id)
        # Sending confirmation and updated data
        AllianceEventMessage(self.client, self.player, 81).Send()
        AllianceEventMessage(self.client, self.player, 101).SendTo(self.targetID[1])