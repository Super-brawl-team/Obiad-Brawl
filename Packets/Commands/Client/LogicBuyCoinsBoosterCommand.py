from Logic.Player import Player
from Packets.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Database.DatabaseManager import DataBase
from Utils.Reader import ByteStream
from datetime import datetime, timedelta
class LogicBuyCoinsBoosterCommand(ByteStream):
    def __init__(self, device, player, data):
        super().__init__(data)
        self.player = player
        self.device = device

    def decode(self):
        self.readCommandHeader()

    def process(self):
        db = DataBase(self.player)
        if self.player.gems < 20:
            return "no cheating"
        self.player.gems - 20
        db.replaceValue("gems", self.player.gems)
        current_time = int(datetime.timestamp(datetime.now()))

        if self.player.coinsbooster is None or self.player.coinsbooster < current_time:
            self.player.coinsbooster = current_time + 7 * 24 * 60 * 60
        else:
            self.player.coinsbooster += 7 * 24 * 60 * 60

        db.replaceValue('coinsbooster', self.player.coinsbooster)