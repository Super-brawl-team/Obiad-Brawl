from Packets.Messages.Server.AllianceChatServer import AllianceChatServer
from Packets.Messages.Server.AllianceEventMessage import AllianceEventMessage
from Database.DatabaseManager import DataBase
from Packets.PiranhaMessage import PiranhaMessage
from Packets.Messages.Server.MyAlliance import MyAlliance
from Packets.Messages.Server.ClanStream import ClanStream

class RespondToAllianceJoinRequestMessage(PiranhaMessage):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.fields = {}
        self.fields["messageID"] = self.readLong()
        self.fields["isAccepted"] = self.readBoolean()

    def process(self):
        db = DataBase(self.player)
        newEvent = 2 if self.fields["isAccepted"] else 0
        db.replaceMessageValue(self.fields["messageID"][1], "Event", newEvent)
        db.replaceMessageValue(self.fields["messageID"][1], "PlayerName", self.player.name)
        self.plrids = []
        club =  db.loadClub(self.player.club_id)
        for token in club["info"]["memberCount"]:
            memberData = db.getMemberData(token)
            self.plrids.append(memberData["low_id"])
        for id in self.plrids:
                AllianceChatServer(self.device, self.player,self.player.club_id, self.fields["messageID"][1]+1).SendTo(id)
        if self.fields["isAccepted"]:
            clubMessages = db.loadClubMessages(self.player.club_id)
            playertoken = ""
            if clubMessages != None:
              for index in range(len(clubMessages["info"]["messages"])):
                  if clubMessages["info"]["messages"][str(index)]["Tick"] == self.fields["messageID"][1]:
                      playertoken = db.getTokenByLowId(clubMessages["info"]["messages"][str(index)]["PlayerID"])
                      playerId = clubMessages["info"]["messages"][str(index)]["PlayerID"]
            playersData = db.getSpecifiedPlayers([playertoken])
            playerData = playersData[0]
            if playerData["club_id"] != 0:
                AllianceEventMessage(self.device, self.player, 92).Send()
                return "aa"
            AllianceEventMessage(self.device, self.player, 90).Send()
            self.device.ClientDict["Clients"][str(playerId)]["Player"].club_id = self.player.club_id
            db.replaceOtherValue("club_id", self.player.club_id, playertoken)
            db.replaceOtherValue("club_role", 1, playertoken)
            db.addMember(self.player.club_id, playertoken, 1)
            db.addMsg(self.player.club_id, 4, playerId, playerData["name"], 0, "", 3, playerId)
            MyAlliance(self.device, self.player).SendTo(playerId)
            ClanStream(self.device, self.player).SendTo(playerId)
            self.plrids = []
            nextKey = db.getNextKey(self.player.club_id)
            for token in club["info"]["memberCount"]:
                memberData = db.getMemberData(token)
                self.plrids.append(memberData["low_id"])
            for id in self.plrids:
                    MyAlliance(self.device, self.player).SendTo(id)
                    AllianceChatServer(self.device, self.player, self.player.club_id, nextKey+1).SendTo(id)
            
        else:
            AllianceEventMessage(self.device, self.player, 91).Send()
        