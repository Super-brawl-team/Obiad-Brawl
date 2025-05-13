# -*- coding: utf-8 -*-
from Utils.Writer import Writer

from Logic.Milestones import Milestones
from Database.DatabaseManager import DataBase
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters
import json
from datetime import datetime
class BattleEndSD(Writer):

	def __init__(self, device, player, plrs):
		self.id = 23456
		self.device = device
		self.player = player
		self.plrs = plrs
		self.settings = json.load(open('Settings.json'))
		self.maximumRank = self.settings["MaximumRank"]
		self.maximumUpgradeLevel = self.settings["MaximumUpgradeLevel"]
		self.requiredTrophiesForRank = Milestones.ProgressStartTrophies
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
		if not self.plrs["isInRealGame"] or self.player.tutorialState < 2:
			trophies = 0
			coins = 0
			exp = 0
			star_player_exp = 0
			doubled_coins = 0
			boosted_coins = 0
		else:
			trophies = getBattleEndTrophies(self.plrs["BattleRank"], self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"])
			coins = getBattleEndCoins(self.plrs["BattleRank"])
			exp = getBattleEndExp(self.plrs["BattleRank"])
			star_player_exp = 10
			doubled_coins = coins
			if coins > self.player.coinsdoubler:
				doubled_coins = self.player.coinsdoubler
			self.player.coinsdoubler -= doubled_coins
			db.replaceValue("coinsdoubler", self.player.coinsdoubler)
			boosted_coins = 0
			if self.player.coinsbooster  - int(datetime.timestamp(datetime.now())) > 0:
				boosted_coins = coins
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
		self.writeBoolean(self.player.tutorialState < 2) # is tutorial game
		self.writeBoolean(self.plrs["isInRealGame"]) # is in real game
		self.writeVInt(50) # Coin Booster %
		self.writeVInt(boosted_coins) # Coin Booster Coins Gained
		self.writeVInt(doubled_coins) # Coin Doubler Coins Gained
		
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
		milestonesTrophies = 0
		self.settings = json.load(open('Settings.json'))
		self.maximumRank = self.settings["MaximumRank"]
		Goal0Index = self.maximumRank - 1
		trophiesList = Milestones.ProgressStartTrophies
		for MilestoneIndex in range(Goal0Index):
			if MilestoneIndex >= 34:
				trophiesList.append(trophiesList[33]+50*(MilestoneIndex - 33))
		for x in range(len(trophiesList) - 1):
			if trophiesList[x] <= self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] < trophiesList[x + 1]:
				if trophiesList[x+1 ] <= self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"]+trophies < trophiesList[x + 2]:
					milestonesTrophies += 1
					coins+=10
				break
		milestonesExp = 0
		expList = Milestones.ProgressStartExp
		for x in range(len(expList) - 1):
			if expList[x] <= self.player.player_experience < expList[x + 1]:
				if expList[x+1 ] <= self.player.player_experience + exp+star_player_exp < expList[x + 2]:
					milestonesExp += 1
					coins+=20
				break
		self.writeVInt(milestonesExp + milestonesTrophies) # Count
		for milestone in range(milestonesExp):
			self.writeVInt(5) 
			self.writeVInt(0) 
			self.writeVInt(0) 
			self.writeVInt(0)
			self.writeVInt(0) 
			self.writeVInt(1) 
			self.writeVInt(12) 
			self.writeVInt(20) 
			self.writeScId(5, 1)
		for milestone in range(milestonesTrophies):
			self.writeVint(1)
			self.writeVint(0)
			self.writeVint(0) # Progress Start
			self.writeVint(0) # Progress
			self.writeVint(0)
			self.writeVint(1)
			self.writeVint(1)
			self.writeVint(10)
			self.writeVint(5)
			self.writeVint(1)

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
		self.player.gold += coins + doubled_coins + boosted_coins
		db.replaceValue("gold", self.player.gold)
		self.player.coins_reward = coins + doubled_coins + boosted_coins 
		db.replaceValue("coins_reward", self.player.coins_reward)
		self.player.solo_wins += 1
		db.replaceValue("solo_wins", self.player.solo_wins)
		if self.player.trophies > self.player.highest_trophies:
			self.player.highest_trophies = self.player.trophies
			db.replaceValue("highest_trophies", self.player.highest_trophies)
		
		
class BattleEndTrio(Writer):

	def __init__(self, device, player, plrs):
		self.id = 23456
		self.device = device
		self.plrs = plrs
		self.player = player
		self.settings = json.load(open('Settings.json'))
		self.maximumRank = self.settings["MaximumRank"]
		self.maximumUpgradeLevel = self.settings["MaximumUpgradeLevel"]
		self.requiredTrophiesForRank = Milestones.ProgressStartTrophies
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
				return 10
			elif rang == 1:
				return 5
			elif rang == 2:
				return 0

		db = DataBase(self.player)
		if not self.plrs["isInRealGame"] or self.player.tutorialState < 2:
			trophies = 0
			coins = 0
			exp = 0
			star_player_exp = 0
			doubled_coins = 0
			boosted_coins = 0
		else:
			trophies = getBattleEndTrophies(self.plrs["BattleRank"], self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"])
			coins = getBattleEndCoins(self.plrs["BattleRank"])
			exp = getBattleEndExp(self.plrs["BattleRank"])
			star_player_exp = 10
			doubled_coins = coins
			if coins > self.player.coinsdoubler:
				doubled_coins = self.player.coinsdoubler
			self.player.coinsdoubler -= doubled_coins
			db.replaceValue("coinsdoubler", self.player.coinsdoubler)
			boosted_coins = 0
			if self.player.coinsbooster  - int(datetime.timestamp(datetime.now())) > 0:
				boosted_coins = coins
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
		self.writeBoolean(self.player.tutorialState < 2) # is tutorial game
		self.writeBoolean(self.plrs["isInRealGame"]) # is in real game
		self.writeVInt(50) # Coin Booster %
		self.writeVInt(boosted_coins) # Coin Booster Coins Gained
		self.writeVInt(doubled_coins) # Coin Doubler Coins Gained

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
		milestonesTrophies = 0
		self.settings = json.load(open('Settings.json'))
		self.maximumRank = self.settings["MaximumRank"]
		Goal0Index = self.maximumRank - 1
		trophiesList = Milestones.ProgressStartTrophies
		for MilestoneIndex in range(Goal0Index):
			if MilestoneIndex >= 34:
				trophiesList.append(trophiesList[33]+50*(MilestoneIndex - 33))
		for x in range(len(trophiesList) - 1):
			if trophiesList[x] <= self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] < trophiesList[x + 1]:
				if trophiesList[x+1 ] <= self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"]+trophies < trophiesList[x + 2]:
					milestonesTrophies += 1
					coins+=10
				break
		milestonesExp = 0
		expList = Milestones.ProgressStartExp
		for x in range(len(expList) - 1):
			if expList[x] <= self.player.player_experience < expList[x + 1]:
				if expList[x+1 ] <= self.player.player_experience + exp+star_player_exp < expList[x + 2]:
					milestonesExp += 1
					coins+=20
				break
		self.writeVInt(milestonesExp + milestonesTrophies) # Count
		for milestone in range(milestonesExp):
			self.writeVInt(5) 
			self.writeVInt(0) 
			self.writeVInt(0) 
			self.writeVInt(0)
			self.writeVInt(0) 
			self.writeVInt(1) 
			self.writeVInt(12) 
			self.writeVInt(20) 
			self.writeScId(5, 1)
		for milestone in range(milestonesTrophies):
			self.writeVint(1)
			self.writeVint(0)
			self.writeVint(0) # Progress Start
			self.writeVint(0) # Progress
			self.writeVint(0)
			self.writeVint(1)
			self.writeVint(1)
			self.writeVint(10)
			self.writeVint(5)
			self.writeVint(1)


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
		self.player.gold += coins +boosted_coins+doubled_coins
		db.replaceValue("gold", self.player.gold)
		self.player.coins_reward = coins+boosted_coins+doubled_coins
		db.replaceValue("coins_reward", self.player.coins_reward)
		self.player.three_vs_three_wins += 1
		db.replaceValue("three_vs_three_wins", self.player.three_vs_three_wins)
		if self.player.trophies > self.player.highest_trophies:
			self.player.highest_trophies = self.player.trophies
			db.replaceValue("highest_trophies", self.player.highest_trophies)
		# Milestones Array
		self.writeBool(True) # Bool
		Milestones.MilestonesArray(self)