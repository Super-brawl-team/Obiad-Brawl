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


class OwnHomeDataMessage(Writer):

	def __init__(self, device, player):
		self.id = 24101
		self.device = device
		self.player = player
		super().__init__(self.device)

	def encode(self):
		skins = Skins().getSkins()
		UnlockCards = Cards().getBrawlers()
		Brawlers228 = Characters().getBrawlers()
		cards = Cards().getCards()
		ressources_ids = [1, 5, 6]
		self.settings = json.load(open('Settings.json'))
		self.maximumRank = self.settings["MaximumRank"]
		self.maximumUpgradeLevel = self.settings["MaximumUpgradeLevel"]
		self.requiredTrophiesForRank = ProgressStart = [0,10,20,30,40,60,80,100,120,140,160,180,220,260,300,340,380,420,460,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200]
		if self.maximumRank <= 34:
			self.brawlersTrophies = self.requiredTrophiesForRank[self.maximumRank-1]
		else:
			self.brawlersTrophies = self.requiredTrophiesForRank[33] + (50* (self.maximumRank-34))
		self.writeVInt(2017189) # Timestamp
		self.writeVInt(10) # Create new band timer
		
		self.writeVInt(self.brawlersTrophies * len(Brawlers228))  # Trophies
		self.writeVInt(self.brawlersTrophies * len(Brawlers228))  # Highest Trophies
		
		self.writeVInt(69696969)  # Experience
		
		self.writeScID(28, 0)  # Player Icon
		self.writeVInt(7) # Played Game Modes Count
		for x in range(7): 
			self.writeVInt(x) # Played Game Mode
		
		self.writeVInt(0) # selected skin count
		for x in range(0):
			self.writeScID(29, x) # Selected Skin
		
		self.writeVInt(len(skins)) # unlocked skin count
		for x in range(len(skins)):
			self.writeScID(29, skins[x]) # unlocked Skin
		
		self.writeBool(True) # is time required to create new Band
		self.writeVInt(0) # unknown bruh
		self.writeVInt(69) # coins got
		self.writeVInt(0) # Control Mode [0 - Tap to move, 1 - Joystick move, 2 - Double Joysticks (prototype)]
		self.writeBool(False) # is battle hints enabled
		self.writeVInt(6974) # coins doubler coins remaining (0 = not activated)
		self.writeVInt(777) # coin boost secs remaining (0 = not activated)
		self.writeBool(False) # unknown
		self.writeVInt(2017189)  # Shop Timestamp
		self.writeVInt(100) # box cost (gold)
		self.writeVInt(10) # box cost (gems)
		self.writeVInt(20) # Coin Boost cost
		self.writeVInt(50) # Coin Boost %
		self.writeVInt(50) # Coin Doubler cost
		self.writeVInt(1000) # Coin Doubled
		self.writeVInt(14) # Coin Boost Days
		self.writeVInt(1) # unknown bruh
		self.writeVInt(2) # unknown bruh
		self.writeVInt(10) # unknown bruh
		self.writeVInt(60) # unknown bruh
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
			self.writeVInt(777) # coins to win
			self.writeVInt(3) # event type , 1= double coins (??) 2+ = double xp 3 = double coins + exp

			self.writeScID(15, random.randint(0, len(Locations().GetLocations()) - 1)) # map
			self.writeVInt(69) #  coins already collected
			self.writeVInt(2) #  coins collected statut
			self.writeString("Server by PrimoDEVHacc") # text for event (TID)
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
			self.writeVInt(60) # coins to win
			self.writeVInt(2) # event type , 1= double coins (??) 2+ = double xp 3 = double coins + exp
			self.writeScID(15, random.randint(0, len(Locations().GetLocations()) - 1)) # map
			self.writeVInt(0) #  coins already collected
			self.writeVInt(2) #  coins collected statut
			self.writeString("This event is comming soon") # text for event (TID)
			if self.player.usedVersion >= 2:
				self.writeBoolean(False)
		# comming soon event ends
			
		# Events array ends
		
		self.writeVInt(self.maximumUpgradeLevel) # upgrades Array
		for x in range(self.maximumUpgradeLevel):
			self.writeVInt(x + 1) # price
		
		Milestones.MilestonesArray(self)
		
		
		self.writeLong(self.player.HighID, self.player.LowID)  # Player id
		
		for id in range(3):
			self.writeLogicLong(self.player.HighID, self.player.LowID) # Player ids related to home menu
		
		self.writeString(self.player.name)
		self.writeBool(True) # nameSet
		self.writeInt(1) # Player region ?
		
		# motorised arrays stars 
		self.writeVInt(5) # Commodity Array
		
		self.writeVInt(len(cards) + len(ressources_ids)) # cards and ressources array
		
		for i in range(len(cards)):
			self.writeScId(23, i)
			
			if i in UnlockCards:
				self.writeVInt(1) # brawler unclocked
			else:
				self.writeVInt(self.maximumUpgradeLevel) # upgrades count
        
        # ressources
		for res in range(len(ressources_ids)):
			self.writeScID(5, ressources_ids[res]) # resource 
			self.writeVInt(99999) # count
         
        # cards and ressources Array End
		
		self.writeVInt(len(Brawlers228)) # brawlers
		for x in Brawlers228:  # trophis
			self.writeVInt(16) # csvID
			self.writeVInt(x) # brawlerID
			self.writeVInt(self.brawlersTrophies) # trophis
		
		self.writeVInt(len(Brawlers228)) # brawlers
		for x in Brawlers228:  # trophis for rank
			self.writeVInt(16) # csvID
			self.writeVInt(x) # brawlerID
			self.writeVInt(self.brawlersTrophies) # trophis for rank	
		
		self.writeVInt(0) # array
		self.writeVInt(0) # array
		
		self.writeVInt(6969) # gems
		self.writeVInt(13) # free gems (?) 
		
		self.writeVInt(0)
		self.writeVInt(0)
		self.writeVInt(0)
		self.writeVInt(0)
		self.writeVInt(0)
		self.writeVInt(0)
		self.writeVInt(0)
		self.writeVInt(0)
		
		self.writeVInt(2) # tutorial state
		self.writeVInt(2017189) # dudka timestamps from hell