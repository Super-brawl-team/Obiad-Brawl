# -*- coding: utf-8 -*-
from Logic import Milestones
from Logic.Player import Player
from Utils.Writer import Writer
from random import randint as r


class OwnHomeData(Writer):

	def __init__(self, device):
		self.id = 24101
		self.device = device
		self.player = Player(device)
		super().__init__(self.device)

	def encode(self):
		skins = 32
		Brawlers228 = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56]
		Upgrades = 60
		self.writeVInt(2017189) # Timestamp
		self.writeVInt(10) # Create new band timer
		
		self.writeVInt(9299)  # Trophies
		self.writeVInt(9292)  # Highest Trophies
		
		self.writeVInt(9999)  # Experience
		
		self.writeScID(28, 2)  # Player Icon
		self.writeVInt(10) # Played Game Modes Count
		for x in range(10): 
			self.writeVInt(x) # Played Game Mode
		
		self.writeVInt(0) # selected skin count
		for x in range(0):
			self.writeScID(29, x) # Selected Skin
		
		self.writeVInt(skins) # unlocked skin count
		for x in range(skins):
			self.writeScID(29, x) # unlocked Skin
		
		self.writeBool(True) # is time required to create new Band
		self.writeVInt(0) # unknown bruh
		self.writeVInt(69) # coins got
		self.writeVInt(2) # Control Mode [0 - Tap to move, 1 - Joystick move, 2 - Double Joysticks (prototype)
		self.writeBool(True) # is battle hints enabled
		self.writeVInt(0) # coins doubler coins remaining (0 = not activated)
		self.writeVInt(0) # coin boost secs remaining (0 = not activated)
		self.writeInt8(22) # Season End timer (????)
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
		# dudka events starts
		
		self.writeVInt(4) # count
		
		self.writeVInt(1) # event #1
		self.writeVInt(0) # Brawlers needed for that
		
		self.writeVInt(2) # event #2
		self.writeVInt(3) # Brawlers needed for that 
		
		self.writeVInt(3) # Event #3
		self.writeVInt(5) # Brawlers needed for that
		
		self.writeVInt(4) # Event #4
		self.writeVInt(8) # Brawlers needed for that
		
		# disponible events starts
		
		self.writeVInt(3) # disponibles event slot
		
		
		
		# first event slot
		
		self.writeVInt(1) # slot index
		self.writeVInt(1) # slot number
		self.writeVInt(1) # comming soon timer
		self.writeVInt(39120) # Time Left
		self.writeVInt(8) # coins to claim
		self.writeVInt(8) # bonuska coins
		self.writeVInt(60) # coins to win
		self.writeVInt(0) # event type , 1= double coins (??) 2+ = double xp 3 = double coins + exp
		self.writeScID(15, 4) # map
		self.writeVInt(0) #  coins already collected
		self.writeVInt(2) #  coins collected statut
		self.writeString() # text for event (TID)
		# first event slot end
		# second event slot
		self.writeVInt(2) # slot index
		self.writeVInt(2) # slot number
		self.writeVInt(1) # comming soon timer
		self.writeVInt(39120) # Time Left
		self.writeVInt(8) # coins to claim
		self.writeVInt(8) # bonuska coins
		self.writeVInt(60) # coins to win
		self.writeVInt(0) # event type , 1= double coins (??) 2+ = double xp 3 = double coins + exp
		self.writeScID(15, 2) # map
		self.writeVInt(0) #  coins already collected
		self.writeVInt(2) #  coins collected statut
		self.writeString() # text for event (TID)
		# second event slot end
		# third event slot
		self.writeVInt(3) # slot index
		self.writeVInt(3) # slot number
		self.writeVInt(1) # comming soon timer
		self.writeVInt(39120) # Time Left
		self.writeVInt(8) # coins to claim
		self.writeVInt(8) # bonuska coins
		self.writeVInt(60) # coins to win
		self.writeVInt(0) # event type , 1= double coins (??) 2+ = double xp 3 = double coins + exp
		self.writeScID(15, 3) # map
		self.writeVInt(0) #  coins already collected
		self.writeVInt(2) #  coins collected statut
		self.writeString() # text for event (TID)
		# third event slot end
		
		# ultra comming soon event starts (it doesn't work bruhh
		self.writeVInt(4) # count
		
		# first comming soon event 
		self.writeVInt(1) # slot index
		self.writeVInt(1) # slot number
		self.writeVInt(1) # comming soon timer
		self.writeVInt(39120) # Time Left
		self.writeVInt(8) # coins to claim
		self.writeVInt(8) # bonuska coins
		self.writeVInt(60) # coins to win
		self.writeVInt(0) # event type , 1= double coins (??) 2+ = double xp 3 = double coins + exp
		self.writeScID(15, 5) # map
		self.writeVInt(0) #  coins already collected
		self.writeVInt(0) #  coins collected statut
		self.writeString() # text for event (TID)
		# first comming soon event  end
		
		# second comming soon event 
		self.writeVInt(2) # slot index
		self.writeVInt(2) # slot number
		self.writeVInt(1) # comming soon timer
		self.writeVInt(39120) # Time Left
		self.writeVInt(8) # coins to claim
		self.writeVInt(8) # bonuska coins
		self.writeVInt(60) # coins to win
		self.writeVInt(0) # event type , 1= double coins (??) 2+ = double xp 3 = double coins + exp
		self.writeScID(15, 5) # map
		self.writeVInt(0) #  coins already collected
		self.writeVInt(0) #  coins collected statut
		self.writeString() # text for event (TID)
		# second comming soon event end
		
		# third comming soon event 
		self.writeVInt(3) # slot index
		self.writeVInt(3) # slot number
		self.writeVInt(1) # comming soon timer
		self.writeVInt(39120) # Time Left
		self.writeVInt(8) # coins to claim
		self.writeVInt(8) # bonuska coins
		self.writeVInt(60) # coins to win
		self.writeVInt(0) # event type , 1= double coins (??) 2+ = double xp 3 = double coins + exp
		self.writeScID(15, 5) # map
		self.writeVInt(0) #  coins already collected
		self.writeVInt(0) #  coins collected statut
		self.writeString() # text for event (TID)
		# third comming soon event end
		
		# fourth comming soon event 
		self.writeVInt(4) # slot index
		self.writeVInt(4) # slot number
		self.writeVInt(1) # comming soon timer
		self.writeVInt(39120) # Time Left
		self.writeVInt(8) # coins to claim
		self.writeVInt(8) # bonuska coins
		self.writeVInt(60) # coins to win
		self.writeVInt(0) # event type , 1= double coins (??) 2+ = double xp 3 = double coins + exp
		self.writeScID(15, 5) # map
		self.writeVInt(0) #  coins already collected
		self.writeVInt(0) #  coins collected statut
		self.writeString("TID_WEEKEND_EVENT") # text for event (TID)
		# fourth comming soon event end
		
		# dudka events end
		self.writeVInt(5) # Unknown Array
		for x in [1, 2, 3, 4, 5]:
			self.writeVInt(x)
		
		self.writeVInt(Milestones.MilestonesCount)  # Milestones Count (518 standart)
		self.writeHexa(Milestones.MilestonesHex)
		
		
		self.writeInt(0)
		self.writeInt(0)  # LongLong
		
		self.writeVInt(0)
		self.writeVInt(0)  # LogicLong
		
		self.writeVInt(0) # Notification Factory array naverno
		
		self.writeVInt(0)  # Empty LogicLong
		self.writeVInt(0)
		self.writeVInt(0)  # Empty LogicLong
		
		self.writeString("PrimoDEVHacc")
		self.writeBool(True) # nameSet
		self.writeInt(0)
		
		# motorised arrays stars 
		self.writeVInt(5) # Commodity Array
		
		self.writeVInt((len(Brawlers228) + 3) + (Upgrades * 3)) # count
		
		for health_id in range(Upgrades):
			self.writeScID(23, health_id) # ?
			self.writeVInt(5) #number of upgrades
		
		for attack_id in range(Upgrades):
			self.writeScID(23, attack_id) # ?
			self.writeVInt(5) #number of upgrades
		
		for ulti_id in range(Upgrades):
			self.writeScID(23, ulti_id) # ?
			self.writeVInt(5) #number of upgrades
		
		self.writeVInt(5) # csv
		self.writeVInt(1) # resource csv
		self.writeVInt(1337) # goldenese
		
		self.writeVInt(5) # csv
		self.writeVInt(5) # resource csv
		self.writeVInt(6974) # elixears
		
		self.writeVInt(5) # csv
		self.writeVInt(6) # resource csv
		self.writeVInt(9999999) # cheaps
		
		for x in Brawlers228:  # Unlocks
			self.writeVInt(23) # csvID
			self.writeVInt(x) # brawlerID
			self.writeVInt(1) # isUnlocked
		
		self.writeVInt(15) # brawlers
		for x in range(15):  # trophis
			self.writeVInt(16) # csvID
			self.writeVInt(x) # brawlerID
			self.writeVInt(1) # trophis
		
		self.writeVInt(15) # brawlers
		for x in range(15):  # trophis for rank
			self.writeVInt(16) # csvID
			self.writeVInt(x) # brawlerID
			self.writeVInt(1) # trophis for rank
		# motorized arrays ENDDDD
		
		
		
		
		self.writeVInt(0) # array
		self.writeVInt(0) # array
		
		self.writeVInt(696969) # gems
		self.writeVInt(0) # free gems (?) 
		
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