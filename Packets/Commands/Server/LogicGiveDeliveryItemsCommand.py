
import random
from Files.CsvLogic.Cards import Cards


class LogicGiveDeliveryItemsCommand:
    def encode(self):
        
          PremierTirage = random.randint(0, 1)
          if PremierTirage == 1:
          
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
          else:
                BrawlersList = Cards().getBrawlers()
                print(f"[x] A box has been opened, here is what ids the reader has got: {BrawlersList}")
                Brawler = (random.choice(BrawlersList))
                Rarity = Cards().getBrawlerRarity(Brawler)
                if Rarity == 'common':
                   RID = 0
                elif Rarity == 'rare':
                   RID = 1
                elif Rarity == 'epic':
                   RID = 2
                else:
                   RID = 3
                self.writeVInt(RID) # Box ID
                self.writeScID(0, 0)
                self.writeVInt(1)
                self.writeScID(23, Brawler)