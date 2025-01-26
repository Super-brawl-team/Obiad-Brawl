from Logic.Player import Player
from Packets.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Database.DatabaseManager import DataBase
from Utils.Reader import ByteStream
class LogicBuyCoinsDoublerCommand(ByteStream):
    def __init__(self, device, player, data):
        super().__init__(data)
        self.player = player
        self.device = device

    def decode(self):
        self.readCommandHeader()

    def process(self):
        db = DataBase(self.player)
        if self.player.gems < 50:
            return "no cheating"
        self.player.gems - 50
        db.replaceValue("gems", self.player.gems)
        self.player.coinsdoubler += 1000
        db.replaceValue("coinsdoubler", self.player.coinsdoubler)