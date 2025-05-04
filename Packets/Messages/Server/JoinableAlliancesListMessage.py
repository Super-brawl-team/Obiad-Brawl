from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
import time
class JoinableAlliancesListMessage(Writer):
           def __init__(self, device, player):
               self.id = 24304
               self.device = device
               self.player = player
               super().__init__(self.device)

           def encode(self):
                db = DataBase(self.player)
                clubs =  db.countClubs(1, 100, 2, 50)
                self.writeVint(len(clubs[0]))
                for club in clubs[1]:
                    
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
                    

                    