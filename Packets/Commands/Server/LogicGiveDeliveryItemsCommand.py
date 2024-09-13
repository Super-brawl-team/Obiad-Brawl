
import random
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
    def decode(self):
        logicGiveDeliveryItemsPayload = {}
        logicGiveDeliveryItemsPayload["rarityID"] = self.readVInt()
        logicGiveDeliveryItemsPayload["itemTypeID"] = self.readDataReference()
        logicGiveDeliveryItemsPayload["rewardAmount"] = self.readVInt()
        logicGiveDeliveryItemsPayload["itemClassID"] = self.readDataReference()
    def process(self):
        pass