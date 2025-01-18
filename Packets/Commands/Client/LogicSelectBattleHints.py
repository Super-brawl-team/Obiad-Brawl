from Logic.Player import Player
from Packets.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Database.DatabaseManager import DataBase
from Utils.Reader import ByteStream

class LogicSelectBattleHintsCommand(ByteStream):
    def __init__(self, device, player, data):
        super().__init__(data)
        self.player = player
        self.device = device

    def decode(self):
        self.readCommandHeader()

    def process(self):
        db = DataBase(self.player)
        self.player.has_battle_hints = not self.player.has_battle_hints
        db.replaceValue("has_battle_hints", self.player.has_battle_hints)
        
