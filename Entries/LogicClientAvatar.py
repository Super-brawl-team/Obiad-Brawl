from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
from Logic.Player import Player

class LogicClientAvatar:
    def encode(self: Writer, player):
        self.player = player
        db = DataBase(self.player)
        ressources_ids = [1, 5, 6]
        ressources = [self.player.gold, self.player.chips, self.player.elexir]
        for id in range(3):
            self.writeLogicLong(self.player.high_id, self.player.low_id) # Player ids related to home menu

        self.writeString(self.player.name)
        self.writeBool(self.player.name != "Brawler") # nameSet
        self.writeInt(1) # Player region ?

        # motorised arrays stars 
        self.writeVInt(5) # Commodity Array
        cards = {}
        for key, brawler in self.player.unlocked_brawlers.items():
            for card, amount in brawler["Cards"].items():
                cards[card] = amount
        self.writeVInt(len(cards) + len(ressources_ids)) # cards and ressources array
        for key, amount in cards.items():
            self.writeScId(23, int(key))
            self.writeVInt(amount) # upgrades count

        # ressources
        for res in range(len(ressources_ids)):
            self.writeScID(5, ressources_ids[res]) # resource 
            self.writeVInt(ressources[res]) # count
            
        # cards and ressources Array End

        self.writeVInt(len(self.player.unlocked_brawlers))  # brawlers count
        for key, brawler_id in self.player.unlocked_brawlers.items():
            self.writeDataReference(16, int(key))
            self.writeVInt(brawler_id["Trophies"])

        # Brawlers Trophies for Rank array
        self.writeVInt(len(self.player.unlocked_brawlers))  # brawlers count
        for key, brawler_id in self.player.unlocked_brawlers.items():
            self.writeDataReference(16, int(key))
            self.writeVInt(brawler_id["HighestTrophies"])

        self.writeVInt(0) # highest ressources array (smart supercell)
        # brawler seen state array
        self.writeVInt(len(self.player.unlocked_brawlers))  # brawlers count
        for key, brawler_id in self.player.unlocked_brawlers.items():
            self.writeDataReference(16, int(key))
            self.writeVInt(2)

        self.writeVInt(self.player.gems) # gems
        self.writeVInt(13) # free gems (?) 

        self.writeVInt(0) # experience level (unused)
        self.writeVInt(0) # cumulative purchased gems
        self.writeVInt(0) # battles couns
        self.writeVInt(0) # win count
        self.writeVInt(0) # lose count
        self.writeVInt(0) # win/loose streak (in v1 yeah)
        self.writeVInt(0) # npc win count
        self.writeVInt(0) # npc lose count

        self.writeVInt(self.player.tutorialState) # tutorial state
        
        self.player.coins_reward = 0
        db.replaceValue("coins_reward", self.player.coins_reward)

