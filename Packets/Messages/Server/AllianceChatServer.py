# -*- coding: utf-8 -*-
from Entries.StreamEntryFactory import StreamEntryFactory
from Database.DatabaseManager import DataBase
from Utils.Writer import Writer

class AllianceChatServer(Writer):
     def __init__(self, device, player, clubLowID, tick):
          self.id = 24312
          self.device = device
          self.tick = tick
          self.player = player
          self.clubLowID = clubLowID
          super().__init__(self.device)

     def encode(self):
          db = DataBase(self.player)
          msgCount = 0
          messageKey = str(0)
          if self.clubLowID != 0:
               clubMessages = db.loadClubMessages(self.clubLowID)
               if clubMessages != None:
                    for index in range(len(clubMessages["info"]["messages"])):
                         if clubMessages["info"]["messages"][str(index)]["Tick"] == self.tick-1:
                              messageKey = str(index)
                    msgCount = 1
          print(msgCount)
          for index in range(msgCount):  # Loop through message indices
          #for index in range(0):
               message = clubMessages["info"]["messages"][messageKey]
               self.writeVInt(message["EventType"])
               StreamEntryFactory.createStreamEntryByType(self, message)
          else:
               self.writeVint(0)  # No messages