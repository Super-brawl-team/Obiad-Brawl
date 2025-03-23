from Packets.Messages.Server.MatchMakingStatusMessage import MatchMakingStatusMessage
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase

class CancelMatchMakingMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        pass
        

    def process(self):
        db = DataBase(self.player)
        matchmaking = db.loadMatchmakingData([self.player.battleID])[0]
        matchmaking["players"].remove(self.player.low_id)
        MatchMakingStatusMessage(self.device, self.player, False).Send()