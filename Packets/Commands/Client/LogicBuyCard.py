from Logic.Player import Player
from Packets.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Database.DatabaseManager import DataBase
from Utils.Reader import ByteStream
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters
import json 
class LogicBuyCardCommand(ByteStream):
    def __init__(self, device, player, data):
        super().__init__(data)
        self.player = player
        self.device = device

    def decode(self):
        self.readCommandHeader()
        self.targetCard = self.readDataReference()
        print(self.targetCard)

    def process(self):
        db = DataBase(self.player)
        self.settings = json.load(open('Settings.json'))
        self.maximumUpgradeLevel = self.settings["MaximumUpgradeLevel"]
        unlock_card = Cards().getUnlock(self.targetCard[1])
        if unlock_card is None:
            return "no cheating"
        if unlock_card != self.targetCard[1]:
            if str(self.targetCard[1]) in self.player.unlocked_brawlers[str(Cards().getbrawlerID(unlock_card))]["Cards"]:
                if self.player.elexir < self.player.unlocked_brawlers[str(Cards().getbrawlerID(unlock_card))]["Cards"][str(self.targetCard[1])]:
                    return "no cheating"
                if self.player.unlocked_brawlers[str(Cards().getbrawlerID(unlock_card))]["Cards"][str(self.targetCard[1])] +1 > self.maximumUpgradeLevel:
                    return "no cheating"
                self.player.unlocked_brawlers[str(Cards().getbrawlerID(unlock_card))]["Cards"][str(self.targetCard[1])] +=1
                self.player.elexir -= self.player.unlocked_brawlers[str(Cards().getbrawlerID(unlock_card))]["Cards"][str(self.targetCard[1])]
            else:
                if self.player.elexir < 1:
                    return "no cheating"
                self.player.unlocked_brawlers[str(Cards().getbrawlerID(unlock_card))]["Cards"][str(self.targetCard[1])] = 1
                
                self.player.elexir -= 1
            db.replaceValue("elexir", self.player.elexir)
        else:
            brawler = Cards().getbrawlerID(unlock_card)
            Rarity = brawler
            
            if Characters.isDisabled(brawler):
                return "no cheating"
            if Rarity == 'common':
                price = 3
            elif Rarity == 'rare':
                price = 10
            elif Rarity == 'epic':
                price = 70
            else:
                price = 600
            if self.player.chips < price:
                return "no cheating"
            self.player.chips -= price
            db.replaceValue("chips", self.player.chips)
            self.player.unlocked_brawlers[brawler] = {
                     'Cards': {unlock_card: 1},
                     'Skins': [0],

                     'selectedSkin': 0,
                     'Trophies': 0,
                     'HighestTrophies': 0,
                     'PowerLevel': 0,
                     'PowerPoints': 0,
                     'State': 0,
                     'StarPower': 0
                  }

        db.replaceValue('unlocked_brawlers', self.player.unlocked_brawlers)
        
        #AvailableServerCommandMessage(self.device, self.player, 203).Send()