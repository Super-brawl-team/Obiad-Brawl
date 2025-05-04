from Utils.Writer import Writer
import random
from Database.DatabaseManager import DataBase
from Entries.StreamEntryFactory import StreamEntryFactory

class TeamStreamMessage(Writer):
    def __init__(self, device, player, tick):
        self.id = 24131
        self.tick = tick
        self.device = device
        self.player = player
        super().__init__(self.device)


    def encode(self):
        """This packet does not exists. Its TeamStreamMessage but i edited it bc i was lazy to code all the logic"""
        self.roomLowID = self.player.teamID
        self.writeLogicLong(0, self.player.teamID)

        db = DataBase(self.player)
        roomMessages = None
        matchedMessages = []

        if self.roomLowID != 0:
            roomMessages = db.loadRoomMessages(self.roomLowID)

        if roomMessages and "info" in roomMessages and "messages" in roomMessages["info"]:
            messages = roomMessages["info"]["messages"]

            # Safely iterate through message dict
            for key, message in messages.items():
                if message.get("Tick") == self.tick:
                    matchedMessages.append(message)

        # Write number of messages that match the tick
        self.writeVInt(len(matchedMessages))

        # Write each matched message
        for message in matchedMessages:
            self.writeVInt(message["EventType"])
            StreamEntryFactory.createStreamEntryByType(self, message)
