# -*- coding: utf-8 -*-

from Utils.Writer import Writer

class ClanStream(Writer):
    def __init__(self, device, player):
         self.id = 24311
         self.device = device
         self.player = player
         super().__init__(self.device)

    def encode(self):
        data = "04-00-82-D5-84-03-01-80-24-00-00-00-06-42-65-72-6B-61-6E-01-BD-D9-0F-00-03-00-04-00-86-8D-98-03-00-84-E6-01-00-00-00-09-EC-95-84-EC-9D-B4-EC-9C-A0-02-BA-A3-0A-00-05-01-01-80-24-00-00-00-06-42-65-72-6B-61-6E-04-00-87-8D-98-03-00-84-E6-01-00-00-00-09-EC-95-84-EC-9D-B4-EC-9C-A0-02-BA-A3-0A-00-04-00"
        self.writeVInt(3) #msg count
        self.writeHexa(data, len(data)) # i have to decrypt this shit