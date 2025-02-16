from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
import time
class MyAlliance(Writer):
           def __init__(self, device, player):
               self.id = 24399
               self.device = device
               self.player = player
               super().__init__(self.device)

           def encode(self):
                db = DataBase(self.player)
                club = db.loadClub(self.player.club_id)
                if self.player.club_id != 0:
                    self.writeVInt(club["info"]["onlineMembers"])
                    self.writeBoolean(True)
                    self.writeDataReference(25, self.player.club_role) # Your role?
                    self.writeLong(0, self.player.club_id) # club id
                    self.writeString(club["info"]["name"])
                    self.writeDataReference(8, club["info"]["clubBadge"]) # club avatar
                    self.writeVInt(club["info"]["clubType"]) # Club type [1 = open, 2 = invite only, 3 = closed]
                    self.writeVInt(club["info"]["onlineMembers"]) # players count
                    self.writeVInt(club["info"]["trophies"]) # club trophies
                    self.writeDataReference(0, 1) # unk dataref
                    self.writeVInt(len(club["info"]["memberCount"])) # club players array naverno
                    
                else:
                    self.writeVInt(0)
                    self.writeBoolean(False)
                
                