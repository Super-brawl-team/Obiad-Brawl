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
        self.writeHexa("04") # Messages count (4)
        self.writeHexa("04-00-06-00-0F-00-00-00-06") # TODO (unk)
        self.writeHexa("42-65-72-6B-61-6E") # name (Berkan)
        self.writeHexa("01") # pretty sure its the role (1)
        self.writeHexa("9A-4A") # idk what is it (unk)
        self.writeHexa("00") # hmm (0)
        self.writeHexa("03") # type (3 = joined)
        self.writeHexa("42-65-72-6B-61-6E") # name (Berkan)
        self.writeHexa("01") # pretty sure its the role (1)
        self.writeHexa("95-4A-00-00-00-00-0D") # TODO (unk)
        self.writeHexa("53-75-70-20-43-68-69-65-66-20-50-61-74") # message (sup chief pat)
        self.writeHexa("04-00-08-01-13-00-00-00-05") # TODO (unk)
        self.writeHexa("6F-75-61-69-6C") # name (ouail)
        self.writeHexa("01") # pretty sure its the role (1)
        self.writeHexa("B5-47") # idk what is it (unk)
        self.writeHexa("00") # hmm (0)
        self.writeHexa("03") # type (3 = joined)
        self.writeHexa("00-02-00-09-00-0F-00-00-00-06") # TODO (unk)
        self.writeHexa("42-65-72-6B-61-6E") # name (Berkan)
        self.writeHexa("01") # pretty sure its the role (1)
        self.writeHexa("A4-47-00-00-00-00-02") # TODO (unk)
        self.writeHexa("59-6F") # message (Yo)