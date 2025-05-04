from Packets.Messages.Server.TeamStreamMessage import TeamStreamMessage
import random
from Logic.Player import Player
from Utils.Reader import ByteStream
from Database.DatabaseManager import DataBase

class TeamChatMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        self.messageContent = self.readString()


    def process(self):
        db = DataBase(self.player)
        
        db.addGameroomMsg(self.player.teamID, 2, self.player.low_id, self.player.name, self.messageContent, 0)
        tick = db.getNextGameroomKey(self.player.teamID)
        db.loadGameroom()
        gameroomInfo = db.getGameroomInfo("info")
        for player_key, values in gameroomInfo["players"].items():
            TeamStreamMessage(self.device, self.player, tick).SendTo(player_key)