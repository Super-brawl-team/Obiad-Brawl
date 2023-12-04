from Utils.Writer import Writer

class ClanData(Writer):
           def __init__(self, device, player):
               self.id = 24399
               self.device = device
               self.player = player
               super().__init__(self.device)

           def encode(self):
               isInClub = True
               if isInClub:
                      self.writeVInt(0) # high id
                      self.writeInt8(1) # low id
			
                      self.writeScID(25, 2) # Your role
                      self.writeInt(0) # ?
                      self.writeInt(1) # ?
                      self.writeString("<cee1200>P<ce47600>r<cdada00>i<cdada00>m<c6deb0b>o<c00fc16> <c00fc16>T<c217e88>e<c4200fa>a<c4200fa>m</c>")
                      self.writeScID(8, 1) # club avatar
                      self.writeVInt(10) # ?
                      self.writeVInt(1) # players count
                      self.writeVInt(999999) # club trophies
                      self.writeVInt(0) # club players array naverno
                      for x in range(1):
                              self.writeInt(0)
                              self.writeInt(1)
                              self.writeString("<cee1200>P<ce85400>r<ce19700>i<cdada00>m<cdada00>o<c92e507>D<c49f00e>E<c00fc16>V<c00fc16>H<c16a862>a<c2c54ae>c<c4200fa>c</c>")  # name
                              self.writeVInt(1)
                              self.writeVInt(0)
                              self.writeVInt(1000) # trophies
                              self.writeVInt(0) # state
                              self.writeVInt(0)
                              self.writeVInt(0)
                              self.writeVInt(0)
				
				
               else:
                      self.writeBool(False) # is in club
                      self.writeVInt(0) # club data array