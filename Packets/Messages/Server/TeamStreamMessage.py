from Utils.Writer import Writer
import random


class TeamStreamMessage(Writer):
    def __init__(self, device, player):
        self.id = 24131
        self.device = device
        self.player = player
        super().__init__(self.device)


    def encode(self):
            
        if self.player.room_id != 0:
            self.writeLogicLong(0, self.player.teamID) # team id

            # messages array
            self.writeVInt(self.player.teamStreamMessageCount) # amount of messages in the chat
            for msg in range(self.player.teamStreamMessageCount):
                self.writeVInt(0) #type
                self.writeLogicLong(0, 1)
                self.writeLogicLong(0, 1)
                self.writeString(self.player.name)
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeVInt(0)
            # Players Array End