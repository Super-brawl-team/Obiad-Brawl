from Packets.Messages.Server.MyAlliance import MyAlliance
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.AllianceChatServer import AllianceChatServer
from Packets.Messages.Server.AllianceEventMessage import AllianceEventMessage
class AllianceKickMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        self.targetID = self.readLong()
        bruh = self.readString() # Weird ass and useless TID (coc leftover)

    def process(self):
        if self.player.club_id == 0 or self.player.club_role == 1:
            return "kek"
        
        db = DataBase(self.player)
        AllianceEventMessage(self.device, self.player, 100).SendTo(self.targetID[1])
        AllianceEventMessage(self.device, self.player, 70).Send()
        
        playerToken = db.getTokenByLowId(self.targetID[1])
        db.addMember(self.player.club_id, playerToken, 2)
        self.players = db.getAllPlayers()
        for player in self.players:
            if player["low_id"] == self.targetID[1]:
                name = player["name"]
        club =  db.loadClub(self.player.club_id)
        db.addMsg(self.player.club_id, 4, self.player.low_id, self.player.name, self.player.club_role, "", 1, self.targetID[1], name)
        self.plrids = []
        nextKey = db.getNextKey(self.player.club_id)
        for token in club["info"]["memberCount"]:
            memberData = db.getMemberData(token)
            self.plrids.append(memberData["low_id"])
        for id in self.plrids:
            
            if id != self.targetID[1]:
                MyAlliance(self.device, self.player).SendTo(id)
                AllianceChatServer(self.device, self.player, self.player.club_id, nextKey+1).SendTo(id)
                
        self.device.ClientDict["Clients"][str(self.targetID[1])]["Player"].club_id = 0
        db.replaceOtherValue("club_id", 0, playerToken)
        MyAlliance(self.device, self.device.ClientDict["Clients"][str(self.targetID[1])]["Player"]).SendTo(self.targetID[1])