from Packets.Messages.Server.TeamMessage import TeamMessage
from Utils.Reader import ByteStream
from Database.DatabaseManager import DataBase
import time
from Packets.Messages.Server.TeamStreamMessage import TeamStreamMessage

class TeamCreateMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        self.mapSlot = self.readVInt()
        self.player.map_id = self.readVInt()
        self.roomType = self.readVInt()


    def process(self):
        if self.player.teamID != 0:
            return "nuh uh"
        db = DataBase(self.player)
        db.getRoomId()
        db.replaceValue('teamID', self.player.teamID)
        if self.player.map_id > 100:
            self.player.map_id = 0 

        db.createGameroom(self.roomType, {"info": {"roomID": self.player.teamID, "messages": { "0": {"EventType": 4, "Event": 101, "Tick": 1, "PlayerID": self.player.low_id, "PlayerName": self.player.name, "Message": "", "promotedTeam": 0, "TimeStamp": time.time(), "targetID": self.player.low_id, "targetName": self.player.name}}}})
        
        TeamMessage(self.device, self.player).Send()
        TeamStreamMessage(self.device, self.player).Send()