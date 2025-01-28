from Logic.Player import Player
from Packets.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Database.DatabaseManager import DataBase
from Utils.Reader import ByteStream
from Files.CsvLogic.Skins import Skins
import json
class LogicUnlockSkinCommand(ByteStream):
    def __init__(self, device, player, data):
        super().__init__(data)
        self.player = player
        self.device = device

    def decode(self):
        self.readCommandHeader()
        self.fields = {}
        self.fields["skin"] = self.readDataReference()

    def process(self):
        if self.fields["skin"][1] not in Skins().getSkins():
            return "no cheating"
        self.fields["isBrawler"] = Skins().getIsDefaultSkin(self.fields["skin"][1])
        self.fields["brawler"] = Skins().getBrawler(self.fields["skin"][1])
        if self.fields["isBrawler"]:
            return "no cheating"
        else:
            db = DataBase(self.player)
            if str(self.fields["brawler"]) not in self.player.unlocked_brawlers:
                return "kek"
            price = int(Skins().getSkinPrice(self.fields["skin"][1]))
            self.player.gems -= price
            if self.player.gems < price:
                return "no cheating"
            db.replaceValue("gems", self.player.gems)
            self.player.unlocked_brawlers[str(self.fields["brawler"])]["Skins"].append(self.fields["skin"][1])
            self.player.unlocked_brawlers[str(self.fields["brawler"])]["selectedSkin"] = self.fields["skin"][1]
            db.replaceValue('unlocked_brawlers', self.player.unlocked_brawlers)
