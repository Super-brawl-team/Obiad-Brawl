
import random
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
<<<<<<< Updated upstream
=======
from Files.CsvLogic.Cards import Cards
from Utils.Reader import ByteStream
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b

class LogicGiveDeliveryItemsCommand(ByteStream):
    def __init__(self, device, player, data):
        super().__init__(data)
        self.player = player
        self.device = device
    def encode(self):
        
<<<<<<< HEAD
          PremierTirage = random.randint(0, 1)
          if PremierTirage == 1:
=======
>>>>>>> Stashed changes
from Files.CsvLogic.Cards import Cards
from Utils.Reader import ByteStream

class LogicGiveDeliveryItemsCommand(ByteStream):
    def __init__(self, device, player, data):
        super().__init__(data)
        self.player = player
        self.device = device
    def encode(self):
        
          randomValue1 = random.randint(0, 1)
          if randomValue1 == 1:
<<<<<<< Updated upstream
=======
>>>>>>> Stashed changes
=======
          randomValue1 = random.randint(0, 1)
          if randomValue1 == 1:
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
          
                Elixir = random.randint(0, 3)
                if Elixir == 0:
                   Amount = 1
                   Rarity = 0
                elif Elixir == 1:
                   Amount = 2
                   Rarity = 1
                elif Elixir == 2:
                   Amount = 5
                   Rarity = 2
                elif Elixir == 3:
                   Amount = 10
                   Rarity = 3
            
           
                self.writeVInt(Rarity) # rarity
                self.writeScID(5, 6) # item type
                self.writeVInt(Amount) # amount
                self.writeVInt(0) # item given
          else:
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
<<<<<<< Updated upstream
                Brawler = (random.randint(0, 15) * 4)
                self.writeVInt(1) # Box ID
                self.writeScID(0, 0)
                self.writeVInt(1)
                self.writeScID(23, Brawler)
=======
>>>>>>> Stashed changes
                BrawlersList = Cards().getBrawlers()
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
<<<<<<< Updated upstream
=======
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
=======
                BrawlersList = Cards().getBrawlers()
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
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
    def decode(self):
        logicGiveDeliveryItemsPayload = {}
        logicGiveDeliveryItemsPayload["rarityID"] = self.readVInt()
        logicGiveDeliveryItemsPayload["itemTypeID"] = self.readDataReference()
        logicGiveDeliveryItemsPayload["rewardAmount"] = self.readVInt()
        logicGiveDeliveryItemsPayload["itemClassID"] = self.readDataReference()
    def process(self):
<<<<<<< Updated upstream
        pass
=======
<<<<<<< HEAD
        pass
>>>>>>> Stashed changes
=======
        pass
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
