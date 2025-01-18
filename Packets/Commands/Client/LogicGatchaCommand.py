from Logic.Player import Player
from Packets.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Database.DatabaseManager import DataBase
from Utils.Reader import ByteStream

class LogicGatchaCommand(ByteStream):
    def __init__(self, device, player, data):
        super().__init__(data)
        self.player = player
        self.device = device

    def decode(self):
        self.readCommandHeader()
        self.isUsingCoins = self.readBoolean()

    def process(self):
        db = DataBase(self.player)
        if self.isUsingCoins:
            if self.player.gold < 100:
                return "no cheating lol"
            self.player.gold -= 100
            db.replaceValue("gold", self.player.gold)
        else:
            if self.player.gems < 10:
                return "no cheating lol"
            self.player.gems -= 10
            db.replaceValue("gems", self.player.gems)
        
        AvailableServerCommandMessage(self.device, self.player, 203).Send()