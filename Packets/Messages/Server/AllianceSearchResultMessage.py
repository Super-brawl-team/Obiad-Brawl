from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
import time
class AllianceSearchResultMessage(Writer):
           def __init__(self, device, player, fields, count):
               self.id = 24310
               self.device = device
               self.player = player
               self.fields = fields
               self.count = count
               super().__init__(self.device)

           def encode(self):
                db = DataBase(self.player)
                self.writeString(self.fields["RequestedName"])
                self.writeVint(len(self.count))
                for club in self.count:
                    self.writeLong(0, club["info"]["clubID"]) # club id
                    self.writeString(club["info"]["name"])
                    self.writeDataReference(8, club["info"]["clubBadge"]) # club avatar
                    self.writeVInt(club["info"]["clubType"]) # Club type [1 = open, 2 = invite only, 3 = closed]
                    self.writeVInt(len(club["info"]["memberCount"])) # players count
                    trophies = 0
                    for token in club["info"]["memberCount"]:
                        memberData = db.getMemberData(token)
                        trophies += memberData["trophies"]
                    self.writeVInt(trophies) # club trophies
                    self.writeVInt(club["info"]["requiredTrophies"]) # club trophies
                    self.writeDataReference(0, 1) # unk dataref
                    self.writeVInt(len(club["info"]["memberCount"])) # club players array naverno
                    

                    