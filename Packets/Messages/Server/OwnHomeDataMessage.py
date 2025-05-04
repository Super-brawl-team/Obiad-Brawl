# -*- coding: utf-8 -*-
from Logic.Milestones import Milestones
from Logic.Player import Player
from Utils.Writer import Writer
import random
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Locations import Locations
import json
from Database.DatabaseManager import DataBase
from datetime import datetime
class OwnHomeDataMessage(Writer):

	def __init__(self, device, player):
		self.id = 24101
		self.device = device
		self.player = player
		super().__init__(self.device)

	def encode(self):
		db = DataBase(self.player)
		db.loadAccount()
		skins = Skins().getSkins()
		UnlockCards = Cards().getBrawlers()
		Brawlers228 = Characters().getBrawlers()
		cards = Cards().getCards()
		ressources_ids = [1, 5, 6]
		ressources = [self.player.gold, self.player.chips, self.player.elexir]
		self.settings = json.load(open('Settings.json'))
		self.maximumRank = self.settings["MaximumRank"]
		self.maximumUpgradeLevel = self.settings["MaximumUpgradeLevel"]
		self.requiredTrophiesForRank = ProgressStart = [0,10,20,30,40,60,80,100,120,140,160,180,220,260,300,340,380,420,460,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200]
		if self.maximumRank <= 34:
			self.brawlersTrophies = self.requiredTrophiesForRank[self.maximumRank-1]
		else:
			self.brawlersTrophies = self.requiredTrophiesForRank[33] + (50* (self.maximumRank-34))
		
		self.player.player_status = 2
		db.replaceValue("player_status", self.player.player_status)
		self.writeVInt(2017189) # Timestamp
		self.writeVInt(10) # Create new band timer
		
		self.writeVInt(self.player.trophies)  # Trophies
		self.writeVInt(self.player.highest_trophies)  # Highest Trophies
		
		self.writeVInt(self.player.player_experience)  # Experience
		
		self.writeScID(28, self.player.profile_icon)  # Player Icon
		self.writeVInt(7) # Played Game Modes Count
		for x in range(7): 
			self.writeVInt(x) # Played Game Mode
		non_zero_skins = []
		for brawler in self.player.unlocked_brawlers.values():
			if brawler["selectedSkin"] != 0:
				non_zero_skins.append(brawler["selectedSkin"])
		self.writeVInt(len(non_zero_skins))
		for skin in non_zero_skins:
			self.writeDataReference(29, skin)
		
		non_zero_skins = []
		for brawler in self.player.unlocked_brawlers.values():
			for skin in brawler["Skins"]:
				if skin != 0:
					non_zero_skins.append(skin)
		self.writeVInt(len(non_zero_skins))
		for skin in non_zero_skins:
			self.writeDataReference(29, skin)
		
		self.writeBool(True) # is time required to create new Band
		self.writeVInt(0) # unknown bruh
		self.writeVInt(self.player.coins_reward) # coins got
		self.writeVInt(self.player.control_mode) # Control Mode [0 - Tap to move, 1 - Joystick move, 2 - Double Joysticks (prototype)]
		self.writeBool(self.player.has_battle_hints) # is battle hints enabled
		self.writeVInt(self.player.coinsdoubler) # coins doubler coins remaining (0 = not activated)
		if self.player.coinsbooster - int(datetime.timestamp(datetime.now())) > 0:
			self.writeVInt(self.player.coinsbooster - int(datetime.timestamp(datetime.now()))) # coin boost secs remaining (0 = not activated)
		else:
			self.writeVInt(0)
			self.player.coinsbooster = int(datetime.timestamp(datetime.now()))
			db.replaceValue("coinsbooster", self.player.coinsbooster)
		self.writeBool(False) # unknown
		self.writeVInt(2017189)  # Shop Timestamp
		self.writeVInt(100) # box cost (gold)
		self.writeVInt(10) # box cost (gems)
		self.writeVInt(20) # Coin Boost cost
		self.writeVInt(50) # Coin Boost %
		self.writeVInt(50) # Coin Doubler cost
		self.writeVInt(1000) # Coin Doubled
		self.writeVInt(7*24) # Coin Boost Hours
		self.writeVInt(1) # default brawler chips
		self.writeVInt(2) # rare brawler chips
		self.writeVInt(10) # epic brawler chips
		self.writeVInt(60) # legendary brawler chips
		self.writeVInt(3) # default brawler cost
		self.writeVInt(10) # rare brawler cost
		self.writeVInt(70) # epic brawler
		self.writeVInt(600) # legendary brawler cost
		
		# Events array starts

		# Brawlers required for events starts

		self.writeVInt(self.player.eventCount) # count

		requiredBrawlers = [0, 3, 5, 8]

		for event in range(self.player.eventCount):
			self.writeVInt(event + 1) # event index
			self.writeVInt(requiredBrawlers[event]) # Brawlers needed for that

		# Brawlers required for events ends
		
		# disponible events starts
		
		self.writeVInt(self.player.eventCount) # disponibles event slot
		for events in range(self.player.eventCount):
			self.writeVInt(events + 1) # slot index
			self.writeVInt(events + 1) # slot number
			self.writeVInt(1) # comming soon timer
			self.writeVInt(39120) # Time Left
			self.writeVInt(8) # coins to claim
			self.writeVInt(8) # bonuska coins
			self.writeVInt(9999999999) # coins to win
			#self.writeVInt(3) # event type , 1= double coins (??) 2+ = double xp 3 = double coins + exp why did this even worked
			self.writeBoolean(False) # double coins
			self.writeBoolean(event == 4) # double exp
			while True:
				map = random.randint(0, len(Locations().GetLocations()) - 1)
				if map != 20:
					break
			self.writeScID(15, map) # map
			self.writeVInt(0) #  coins already collected
			self.writeVInt(2) #  coins collected statut
			self.writeString("Server by PrimoDEVHacc") # text for event (TID) please keep it for credits
			if self.player.usedVersion >= 2:
				self.writeBoolean(False)

		# disponible events ends
		
		# comming soon events starts
		self.writeVInt(4) # disponibles event slot
		for events in range(4):
			self.writeVInt(events+1) # slot index
			self.writeVInt(events+1) # slot number
			self.writeVInt(1337) # comming soon timer
			self.writeVInt(39120) # Time Left
			self.writeVInt(8) # coins to claim
			self.writeVInt(8) # bonuska coins
			self.writeVInt(9999999999) # coins to win
			#self.writeVInt(2) # event type , 1= double coins (??) 2+ = double xp 3 = double coins + exp
			self.writeBoolean(False) # double coins
			self.writeBoolean(event == 4) # double exp
			while True:
				map = random.randint(0, len(Locations().GetLocations()) - 1)
				if map != 20:
					break
			self.writeScID(15, map) # map
			self.writeVInt(0) #  coins already collected
			self.writeVInt(2) #  coins collected statut
			self.writeString("Server by PrimoDEVHacc") # text for event (TID) please keep it for credits
			if self.player.usedVersion >= 2:
				self.writeBoolean(False)
		# comming soon event ends
			
		# Events array ends
		
		self.writeVInt(self.maximumUpgradeLevel) # upgrades Array
		for x in range(self.maximumUpgradeLevel):
			self.writeVInt(x + 1) # price
		
		Milestones.MilestonesArray(self)
		
		
		self.writeLong(self.player.high_id, self.player.low_id)  # Player id
		
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
		
		self.writeVInt(2) # tutorial state
		self.writeVInt(2017189) # dudka timestamps from hell
		self.player.coins_reward = 0
		db.replaceValue("coins_reward", self.player.coins_reward)