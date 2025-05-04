from Utils.Reader import ByteStream
from random import choice
from string import ascii_uppercase
import json
from Logic.Player import Player
from Packets.Messages.Server.LeaderboardMessage import LeaderboardMessage
from Database.DatabaseManager import DataBase
class GetLeaderboardMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.fields = {}
        self.fields["isLocal"] = self.readVInt()
        self.fields["leaderboardType"] = self.readVInt()
        self.fields["targetBrawler"] = self.readDataReference()


    def process(self):
       db = DataBase(self.player)
       if self.fields["leaderboardType"] == 0:

            def by_brawler_trophy(plr):
                try:
                    brawlerTrophies = plr['unlocked_brawlers'][str(self.fields["targetBrawler"][1])]["Trophies"]
                    return brawlerTrophies
                except:
                    return 0
            self.fields["entries"] = [
    player for player in db.getAllPlayers()
    if str(self.fields["targetBrawler"][1]) in player.get("unlocked_brawlers", {}) and
        player['unlocked_brawlers'][str(self.fields["targetBrawler"][1])]["Trophies"] > 0]
            self.fields["entries"].sort(key=by_brawler_trophy, reverse=True)
            if self.fields["isLocal"]:
                self.fields["entries"] = [
        player for player in self.fields["entries"]
        if player.get("region") == self.player.region
    ]

       elif self.fields["leaderboardType"] == 1:

            def by_trophy(plr):
                return plr['trophies']
            self.fields["entries"] = db.getAllPlayers()
            self.fields["entries"].sort(key = by_trophy, reverse=True)

            if self.fields["isLocal"]:
                for player in self.fields["entries"]:
                    if player["region"] != self.player.region:
                        self.fields["entries"].remove(player)

       elif self.fields["leaderboardType"] == 2:
            clubs = db.countClubs(1, 100, 2, 200)
            self.fields["entries"] = []
            index = 0
            for club in clubs[1]:
                self.fields["entries"].append(club["info"])
                trophies = 0
                for token in club["info"]["memberCount"]:
                    memberData = db.getMemberData(token)
                    trophies += memberData["trophies"]
                self.fields["entries"][index]["trophies"] = trophies
                index +=1
            def by_trophy(club):
                return club["trophies"]
            self.fields["entries"].sort(key=by_trophy, reverse=True)
            if self.fields["isLocal"]:
                self.fields["entries"] = [
        club for club in self.fields["entries"] if club["region"] == self.player.region
    ]
       LeaderboardMessage(self.device, self.player, self.fields).Send()

