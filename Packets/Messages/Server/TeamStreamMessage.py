from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
from Entries.StreamEntryFactory import StreamEntryFactory

class TeamStreamMessage(Writer):
    def __init__(self, device, player):
        self.id = 24131
        self.device = device
        self.player = player
        super().__init__(self.device)


    def encode(self):
        self.roomLowID = self.player.teamID
        self.writeLogicLong(0, self.player.teamID)
        db = DataBase(self.player)
        msgCount = 0
        if self.roomLowID != 0:
            roomMessages = db.loadRoomMessages(self.roomLowID)
            if roomMessages != None:
                msgCount = len(roomMessages["info"]["messages"])
            self.writeVInt(msgCount)  # Message count
            #self.writeVInt(0)

            for index in range(msgCount):  # Loop through message indices
            #for index in range(0):
                messageKey = str(index)
                message = roomMessages["info"]["messages"][messageKey]
                self.writeVInt(message["EventType"])
                StreamEntryFactory.createStreamEntryByType(self, message)
        else:
            self.writeVInt(0)  # No messages