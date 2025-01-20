# -*- coding: utf-8 -*-
from Utils.Writer import Writer

from Logic.Milestones import Milestones
from Database.DatabaseManager import DataBase
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters
import json
class BattleEndSD(Writer):

	def __init__(self, device, player, plrs):
		self.id = 23456
		self.device = device
		self.player = player
		self.plrs = plrs
		Brawlers228 = Characters().getBrawlers()
		cards = Cards().getCards()
		self.settings = json.load(open('Settings.json'))
		self.maximumRank = self.settings["MaximumRank"]
		self.maximumUpgradeLevel = self.settings["MaximumUpgradeLevel"]
		self.requiredTrophiesForRank = ProgressStart = [0,10,20,30,40,60,80,100,120,140,160,180,220,260,300,340,380,420,460,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200]
		if self.maximumRank <= 34:
				self.brawlersTrophies = self.requiredTrophiesForRank[self.maximumRank-1]
		else:
				self.brawlersTrophies = self.requiredTrophiesForRank[33] + (50* (self.maximumRank-34))
		super().__init__(self.device)

	def encode(self):
     	
		def getBattleEndTrophies(rang, trophies):
			
			trophy_ranges = [
				(0, 19, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
				(20, 39, [8, 7, 6, 5, 4, 3, 2, 1, 0, -1]),
				(40, 69, [6, 5, 4, 3, 2, 1, 0, -1, -2, -3]),
				(70, 99, [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]),
				(100, 199, [4, 3, 2, 1, 0, -1, -2, -3, -4, -5]),
				(200, 299, [3, 2, 1, 0, -1, -2, -3, -4, -5, -6]),
				(300, 399, [2, 1, 0, -1, -2, -3, -4, -5, -6, -7]),
				(400, self.brawlersTrophies-1, [1, 0, -1, -2, -3, -4, -5, -6, -7, -8]),
				(self.brawlersTrophies, self.brawlersTrophies, [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]),
				
			]
			for low, high, rank_trophies in trophy_ranges:
				if low <= trophies <= high:
					return rank_trophies[rang-1]
			return 0
		
		def getBattleEndCoins(rang):
			if rang == 10:
				return 1
			elif rang == 9:
				return 1
			elif rang == 8:
				return 2
			elif rang == 7:
				return 4
			elif rang == 6:
				return 6
			elif rang == 5:
				return 8
			elif rang == 4:
				return 12
			elif rang == 3:
				return 16
			elif rang == 2:
				return 22
			elif rang == 1:
				return 28
			elif rang == 0:
				return 34
		
		def getBattleEndExp(rang):
			if rang == 10:
				return 0
			elif rang == 9:
				return 0
			elif rang == 8:
				return 0
			elif rang == 7:
				return 1
			elif rang == 6:
				return 2
			elif rang == 5:
				return 4
			elif rang == 4:
				return 5
			elif rang == 3:
				return 6
			elif rang == 2:
				return 9
			elif rang == 1:
				return 12
			elif rang == 0:
				return 15

		db = DataBase(self.player)
		if not self.plrs["isInRealGame"]:
			trophies = 0
			coins = 0
			exp = 0
			star_player_exp = 0
		else:
			trophies = getBattleEndTrophies(self.plrs["BattleRank"], self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"])
			coins = getBattleEndCoins(self.plrs["BattleRank"])
			exp = getBattleEndExp(self.plrs["BattleRank"])
			star_player_exp = 10
		if self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] + trophies > self.brawlersTrophies:
			trophies = self.brawlersTrophies - self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] 
		self.writeVInt(5) # Battle End Game Mode (5 = Showdown. Else is 3vs3)
		self.writeVInt(0) # Related To Coins Gained. If the Value is 1+, "All Coins collected"
		self.writeVInt(coins) # Coins Gained
		self.writeVInt(6969) # "All Coins collected" if 0, its basically coins left
		self.writeVInt(0) # First Win Coins Gained
		self.writeBool(False) # "All event experience collected" if True
		self.writeVInt(self.plrs["BattleRank"]) # Result (Victory/Defeat/Draw/Rank Score)
		
		self.writeVInt(trophies) # Trophies Result
		self.writeScID(28, self.player.profile_icon)  # Player Profile Icon
		self.writeBoolean(False) # is tutorial game
		self.writeBoolean(self.plrs["isInRealGame"]) # is in real game
		self.writeVInt(0) # Coin Booster %
		self.writeVInt(0) # Coin Booster Coins Gained
		self.writeVInt(0) # Coin Doubler Coins Gained
		
		# Players Array

		self.writeVInt(self.plrs["PlayersAmount"]) # Battle End Screen Players
		for Players in self.plrs["Brawlers"]:
			self.writeString(Players["Name"]) # Player Name
			self.writeBoolean(Players["IsPlayer"]) # is player
			self.writeBoolean(Players["Team"] is not self.plrs["Brawlers"][0]["Team"]) # is ennemy?
			self.writeBoolean(Players["IsPlayer"]) # is star player
			self.writeScID(Players["CharacterID"][0], Players["CharacterID"][1]) # Player Brawler
			self.writeScID(Players["SkinID"][0], Players["SkinID"][1]) # Player Brawler Skin!
			self.writeVInt(0) # Brawler Trophies
		# Experience Array
		self.writeVInt(2) # Count
		self.writeVInt(0) # Normal Experience ID
		self.writeVInt(exp) # Normal Experience Gained
		self.writeVInt(8) # Star Player Experience ID
		self.writeVInt(star_player_exp) # Star Player Experience Gained

		# Rank Up and Level Up Bonus Array
		self.writeVInt(0) # Count

		# Trophies and Experience Bars Array
		self.writeVInt(2) # Count
		self.writeVInt(1) # Trophies Bar Milestone ID
		self.writeVInt(self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"]) # Brawler Trophies
		self.writeVInt(self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"]) # Brawler Trophies for Rank
		self.writeVInt(5) # Experience Bar Milestone ID
		self.writeVInt(self.player.player_experience) # Player Experience
		self.writeVInt(self.player.player_experience) # Player Experience for Level
		
		# Milestones Array
		self.writeBool(True) # Bool

		Milestones.MilestonesArray(self)
		self.player.trophies += trophies
		db.replaceValue("trophies", self.player.trophies)
		self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] += trophies
		if self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] > self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"]:
			self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"] = self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"]
		db.replaceValue("unlocked_brawlers", self.player.unlocked_brawlers)
		self.player.player_experience += exp + star_player_exp
		db.replaceValue("player_experience", self.player.player_experience)
		self.player.gold += coins
		db.replaceValue("gold", self.player.gold)
		self.player.coins_reward = coins 
		db.replaceValue("coins_reward", self.player.coins_reward)
		
		
class BattleEndTrio(Writer):

	def __init__(self, device, player, plrs):
		self.id = 23456
		self.device = device
		self.plrs = plrs
		self.player = player
		Brawlers228 = Characters().getBrawlers()
		cards = Cards().getCards()
		self.settings = json.load(open('Settings.json'))
		self.maximumRank = self.settings["MaximumRank"]
		self.maximumUpgradeLevel = self.settings["MaximumUpgradeLevel"]
		self.requiredTrophiesForRank = ProgressStart = [0,10,20,30,40,60,80,100,120,140,160,180,220,260,300,340,380,420,460,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200]
		if self.maximumRank <= 34:
				self.brawlersTrophies = self.requiredTrophiesForRank[self.maximumRank-1]
		else:
				self.brawlersTrophies = self.requiredTrophiesForRank[33] + (50* (self.maximumRank-34))
		super().__init__(self.device)

	def encode(self):
		def getBattleEndTrophies(rang, trophies):
			
			trophy_ranges = [
				(0, 19, [5, 0, 0]),
				(20, 39, [4, -1, 0]),
				(40, 69, [4, -2, 0]),
				(70, 99, [3, -2, 0]),
				(100, 199, [3, -3, 0]),
				(200, 299, [2, -3, 0]),
				(300, 399, [2, -4, 0]),
				(400, self.brawlersTrophies-1, [1, -4, 0]),
				(self.brawlersTrophies, self.brawlersTrophies, [0, -5, 0]),
				
			]
			for low, high, rank_trophies in trophy_ranges:
				if low <= trophies <= high:
					return rank_trophies[rang]
			return 0
		
		
		def getBattleEndCoins(rang):
			if rang == 0: # win
				return 20
			elif rang == 1:
				return 15
			elif rang == 2:
				return 10

		def getBattleEndExp(rang):
			if rang == 0: # win
				return 0
			elif rang == 1:
				return 5
			elif rang == 2:
				return 10

		db = DataBase(self.player)
		if not self.plrs["isInRealGame"]:
			trophies = 0
			coins = 0
			exp = 0
			star_player_exp = 0
		else:
			trophies = getBattleEndTrophies(self.plrs["BattleRank"], self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"])
			coins = getBattleEndCoins(self.plrs["BattleRank"])
			exp = getBattleEndExp(self.plrs["BattleRank"])
			star_player_exp = 10
		if self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] + trophies > self.brawlersTrophies:
			trophies = self.brawlersTrophies - self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] 
			
		# Star Player State End

		self.writeVInt(1) # Battle End Game Mode (5 = Showdown. Else is 3vs3)
		self.writeVInt(0) # Related To Coins Gained. If the Value is 1+, "All Coins collected"

		self.writeVInt(coins) # Coins Gained
		self.writeVInt(6969) # "All Coins collected" if 0, its basically coins left
		self.writeVInt(0) # First Win Coins Gained
		self.writeBool(False) # "All event experience collected" if True
		self.writeVInt(self.plrs["BattleEndType"]) # Result (Victory/Defeat/Draw/Rank Score)
		self.writeVInt(trophies) # Trophies Result
		self.writeScID(28, self.player.profile_icon)  # Player Profile Icon
		self.writeBoolean(False) # is tutorial game
		self.writeBoolean(self.plrs["isInRealGame"]) # is in real game
		self.writeVInt(0) # Coin Booster %
		self.writeVInt(0) # Coin Booster Coins Gained
		self.writeVInt(0) # Coin Doubler Coins Gained

		# Players Array

		self.writeVInt(self.plrs["PlayersAmount"]) # Battle End Screen Players
		for Players in self.plrs["Brawlers"]:
			self.writeString(Players["Name"]) # Player Name
			self.writeBoolean(Players["IsPlayer"]) # is player
			self.writeBoolean(Players["Team"] is not self.plrs["Brawlers"][0]["Team"]) # is ennemy?
			self.writeBoolean(Players["IsPlayer"]) # is star player
			self.writeScID(Players["CharacterID"][0], Players["CharacterID"][1]) # Player Brawler
			self.writeScID(Players["SkinID"][0], Players["SkinID"][1]) # Player Brawler Skin!
			self.writeVInt(0) # Brawler Trophies
		# Experience Array
		self.writeVInt(2) # Count
		self.writeVInt(0) # Normal Experience ID
		self.writeVInt(exp) # Normal Experience Gained
		self.writeVInt(8) # Star Player Experience ID
		self.writeVInt(star_player_exp) # Star Player Experience Gained

		# Rank Up and Level Up Bonus Array
		self.writeVInt(0) # Count

		# Trophies and Experience Bars Array
		self.writeVInt(2) # Count
		self.writeVInt(1) # Trophies Bar Milestone ID

		self.writeVInt(self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"]) # Brawler Trophies
		self.writeVInt(self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"]) # Brawler Trophies for Rank
		self.writeVInt(5) # Experience Bar Milestone ID
		self.writeVInt(self.player.player_experience) # Player Experience
		self.writeVInt(self.player.player_experience) # Player Experience for Level
		self.player.trophies += trophies
		db.replaceValue("trophies", self.player.trophies)
		self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] += trophies
		if self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] > self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"]:
			self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"] = self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"]
		db.replaceValue("unlocked_brawlers", self.player.unlocked_brawlers)
		self.player.player_experience += exp + star_player_exp
		db.replaceValue("player_experience", self.player.player_experience)
		self.player.gold += coins
		db.replaceValue("gold", self.player.gold)
		self.player.coins_reward = coins
		db.replaceValue("coins_reward", self.player.coins_reward)
		# Milestones Array
		self.writeBool(True) # Bool
		Milestones.MilestonesArray(self)