# -*- coding: utf-8 -*-

from Utils.Writer import Writer

class ClanStream(Writer):
    def __init__(self, device, player):
         self.id = 24311
         self.device = device
         self.player = player
         super().__init__(self.device)

    def encode(self):
        # Crap but i was busy
        self.writeHexa("04-04-00-06-00-0F-00-00-00-06")
        self.writeHexa("42-65-72-6B-61-6E") # name
        self.writeHexa("01-9A-4A-00-03-00-02-00-07-00-0F-00-00-00-06")
        self.writeHexa("42-65-72-6B-61-6E") # name
        self.writeHexa("01-95-4A-00-00-00-00-0D-53-75-70-20-43-68-69-65-66-20-50-61-74-04-00-08-01-13-00-00-00-05-6F-75-61-69-6C-01-B5-47-00-03-00-02-00-09-00-0F-00-00-00-06")
        self.writeHexa("42-65-72-6B-61-6E") # name
        self.writeHexa("01-A4-47-00-00-00-00-02-59-6F") # riiip