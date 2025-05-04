from Packets.Messages.Server.TeamMessage import TeamMessage
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.AllianceChatServer import AllianceChatServer

class TeamPostAdMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        pass
        

    def process(self):
        if self.player.club_id == 0:
            return "wtf?"
        db = DataBase(self.player)
        gamerooomInfo = db.getGameroomInfo("info")
        gamerooomInfo["advertiseToBand"] = not gamerooomInfo["advertiseToBand"]
        gamerooomInfo["advertisedClub"] = [0, self.player.club_id]
        if gamerooomInfo["advertiseToBand"] and not gamerooomInfo["alreadyAdvertisedToBand"]:
            db.addMsg(self.player.club_id, 77, self.player.low_id, self.player.name, self.player.club_role, "", 0)
            gamerooomInfo["alreadyAdvertisedToBand"] = True
            db.updateGameroomInfo(gamerooomInfo["alreadyAdvertisedToBand"], self.player.teamID, "alreadyAdvertisedToBand")
        db.updateGameroomInfo(gamerooomInfo["advertiseToBand"], self.player.teamID, "advertiseToBand")
        gameroomInfo = db.getGameroomInfo("info")
        for player_key, values in gameroomInfo["players"].items():
            TeamMessage(self.device, self.player).SendTo(player_key)
        club =  db.loadClub(self.player.club_id)
        self.plrids = []
        nextKey = db.getNextKey(self.player.club_id)
        for token in club["info"]["memberCount"]:
            memberData = db.getMemberData(token)
            self.plrids.append(memberData["low_id"])
        for id in self.plrids:
                AllianceChatServer(self.device, self.player, self.player.club_id, nextKey+1).SendTo(id)