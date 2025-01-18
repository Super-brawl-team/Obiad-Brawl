# -*- coding: utf-8 -*-
from Entries.StreamEntryFactory import StreamEntryFactory
from Database.DatabaseManager import DataBase
from Utils.Writer import Writer

class ClanStream(Writer):
    def __init__(self, device, player):
         self.id = 24311
         self.device = device
         self.player = player
         super().__init__(self.device)

    def encode(self):
     self.writeVint(0)  # Message count
     for index in range(0):
        self.writeVInt(4) # type
        #StreamEntryFactory.createStreamEntryByType(self, message)