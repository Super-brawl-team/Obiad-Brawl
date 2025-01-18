
import random
<<<<<<< Updated upstream


class LogicGiveDeliveryItemsCommand:
    def encode(self):
        
          PremierTirage = random.randint(0, 1)
          if PremierTirage == 1:
=======
from Files.CsvLogic.Cards import Cards
from Utils.Reader import ByteStream
from Database.DatabaseManager import DataBase
class LogicGiveDeliveryItemsCommand(ByteStream):
    def __init__(self, device, player, data):
        super().__init__(data)
        self.player = player
        self.device = device
    def encode(self):
          db = DataBase(self.player)
          
          randomValue1 = random.randint(0, 1)
          if randomValue1 == 1:
>>>>>>> Stashed changes
          
                Elixir = random.randint(0, 3)
                if Elixir == 0:
                   Nombre = 1
                   Rareté = 0
                elif Elixir == 1:
                   Nombre = 2
                   Rareté = 1
                elif Elixir == 2:
                   Nombre = 5
                   Rareté = 2
                elif Elixir == 3:
                   Nombre = 10
                   Rareté = 3
            
           
                self.writeVInt(Rareté) # rarity
                self.writeScID(5, 6) # item type
                self.writeVInt(Nombre) # amount
                self.writeVInt(0) # item given
                self.player.elexir += Amount
                db.replaceValue("elexir", self.player.elexir)
          else:
<<<<<<< Updated upstream
                Brawler = (random.randint(0, 15) * 4)
                self.writeVInt(1) # Box ID
                self.writeScID(0, 0)
                self.writeVInt(1)
                self.writeScID(23, Brawler)
=======
                BrawlersList = Cards().getBrawlers()
                chipsList = [1, 2, 10, 60]
                Brawler = (random.choice(BrawlersList))
                Rarity = Cards().getBrawlerRarity(Brawler)
                if Rarity == 'common':
                   RarityID = 0
                elif Rarity == 'rare':
                   RarityID = 1
                elif Rarity == 'epic':
                   RarityID = 2
                else:
                   RarityID = 3
                self.writeVInt(RarityID) # rarity ID
                self.writeScID(0, 0)
                self.writeVInt(1)
                self.writeScID(23, Brawler)
                if str(Brawler) not in self.player.unlocked_brawlers:
                   self.player.unlocked_brawlers[Cards().getbrawlerID(Brawler)] = {
                     'Cards': {Brawler: 1},
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
                else:
                   self.player.chips += chipsList[RarityID]
                   db.replaceValue("chips", self.player.chips)
    def decode(self):
        logicGiveDeliveryItemsPayload = {}
        logicGiveDeliveryItemsPayload["rarityID"] = self.readVInt()
        logicGiveDeliveryItemsPayload["itemTypeID"] = self.readDataReference()
        logicGiveDeliveryItemsPayload["rewardAmount"] = self.readVInt()
        logicGiveDeliveryItemsPayload["itemClassID"] = self.readDataReference()
    def process(self):
        pass
>>>>>>> Stashed changes
