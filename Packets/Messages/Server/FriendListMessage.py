# -*- coding: utf-8 -*-
from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class FriendListMessage(Writer):

    def __init__(self, device, player):
        self.id = 20105
        self.device = device
        self.player = player
        super().__init__(self.device)

    def encode(self):
        """Supercell is very picky, the structure is correct but doesnt let me"""
        db = DataBase(self.player)
        player = db.getSpecifiedPlayers([db.getTokenByLowId(1)])[0]
        self.writeInt(0) # friends amount
        self.writeInt(1) # friends again
        for x in range(1):
            self.writeLong(0,1)
            self.writeString(player["name"])
            self.writeString("buh") # faceboook id
            self.writeString("ah") # game center id
            self.writeString() # idk
            self.writeInt(0) # friend state
            self.writeInt(player["trophies"]) # trophies obv
            self.writeInt(0)
            self.writeInt(0)
            self.writeBoolean(player["club_id"]!=0)
            if player["club_id"]!=0:
                club = db.loadClub(player["club_id"])
                self.writeLong(0, player["club_id"])
                self.writeInt(0)
                self.writeString(club["info"]["name"])
                self.writeInt(0)
                self.writeInt(0)
            self.writeString("hai")
            self.writeDataReference(28, 0)