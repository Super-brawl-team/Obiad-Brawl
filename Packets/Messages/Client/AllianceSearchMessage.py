from Packets.Messages.Server.AllianceSearchResultMessage import AllianceSearchResultMessage
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase
from Utils.IdUtils import IdUtils

class AllianceSearchMessage(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.fields = {}
        self.fields["RequestedName"] = self.readString()
        self.fields["Int1"] = self.readInt()
        self.fields["Int2"] = self.readInt()
        self.fields["Int3"] = self.readInt()
        self.fields["Int4"] = self.readInt()
        self.fields["Booolean"] = self.readBoolean()
        self.fields["Int5"] = self.readInt()
        self.fields["Int6"] = self.readInt()

    def process(self):
        db = DataBase(self.player)
        idutils = IdUtils()
        clubs = db.countClubs(1, 100, 2, 30)
        self.foundAlliances = []
        for i in clubs[1]:
            if self.fields["RequestedName"].lower() in i["info"]["name"].lower() or idutils.getHLId(self.fields["RequestedName"].lower())[1] == i["info"]["clubID"]:
                self.foundAlliances.append(i)
        AllianceSearchResultMessage(self.device, self.player, self.fields, self.foundAlliances).Send()