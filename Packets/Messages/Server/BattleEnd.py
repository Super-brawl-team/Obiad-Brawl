from Utils.Writer import Writer
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
from Logic import Milestones


=======
from Logic.Milestones import Milestones
from Database.DatabaseManager import DataBase
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters
import json
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
class BattleEndSD(Writer):

	def __init__(self, device, player):
		self.id = 23456
		self.device = device
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
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
		
		IsMatchmakeBoolean = True
		
		if self.device.BattleResult in [0, 2]:
			if IsMatchmakeBoolean == False:
				IsStarPlayer = 1
			else:
				IsStarPlayer = 5
		else:
			if IsMatchmakeBoolean == False:
				IsStarPlayer = 1
			else:
				IsStarPlayer = 1
		
		self.writeVInt(5) # Battle End Game Mode (5 = Showdown. Else is 3vs3)
		self.writeVInt(0) # Related To Coins Gained. If the Value is 1+, "All Coins collected"
		self.writeVInt(getBattleEndCoins(self.device.rank)) # Coins Gained
		self.writeBool(True) # "All Coins collected" if False
		self.writeVInt(0) # First Win Coins Gained
		self.writeBool(False) # "All event experience collected" if True
		self.writeVInt(self.device.rank) # Result (Victory/Defeat/Draw/Rank Score)
		self.writeVInt(getBattleEndTrophies(self.device.rank)) # Trophies Result
		self.writeScID(28, 0)  # Player Profile Icon
		self.writeVInt(2) # Battle Result Type
=======
		db = DataBase(self.player)
		trophies = getBattleEndTrophies(self.plrs["BattleRank"], self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"])
		if self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] + trophies > self.brawlersTrophies:
			trophies = self.brawlersTrophies - self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] 
		self.writeVInt(5) # Battle End Game Mode (5 = Showdown. Else is 3vs3)
		self.writeVInt(0) # Related To Coins Gained. If the Value is 1+, "All Coins collected"
		self.writeVInt(getBattleEndCoins(self.plrs["BattleRank"])) # Coins Gained
		self.writeVInt(6969) # "All Coins collected" if 0, its basically coins left
		self.writeVInt(0) # First Win Coins Gained
		self.writeBool(False) # "All event experience collected" if True
		self.writeVInt(self.plrs["BattleRank"]) # Result (Victory/Defeat/Draw/Rank Score)
		
		self.writeVInt(trophies) # Trophies Result
		self.writeScID(28, self.player.profile_icon)  # Player Profile Icon
		self.writeBoolean(False) # is tutorial game
		self.writeBoolean(True) # is in real game
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
		self.writeVInt(0) # Coin Booster %
		self.writeVInt(0) # Coin Booster Coins Gained
		self.writeVInt(0) # Coin Doubler Coins Gained
		
		# Players Array
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
		self.writeVInt(1) # Battle End Screen Players
		self.writeString("NostalgicBrawl") # Player Name
		self.writeVInt(IsStarPlayer) # Player Team and Star Player Type
		self.writeScID(16, self.device.brawler) # Player Brawler
		if self.device.skin == 0:
			self.writeVint(0) # Player Skin
		else:
			self.writeScId(29, self.device.skin_id) # Player Skin
		self.writeVInt(1) # Brawler Trophies
=======
		self.writeVInt(self.plrs["PlayersAmount"]) # Battle End Screen Players
		for Players in self.plrs["Brawlers"]:
			self.writeString(Players["Name"]) # Player Name
			self.writeBoolean(Players["IsPlayer"]) # is player
			self.writeBoolean(Players["Team"] is not self.plrs["Brawlers"][0]["Team"]) # is ennemy?
			self.writeBoolean(Players["IsPlayer"]) # is star player
			self.writeScID(Players["CharacterID"][0], Players["CharacterID"][1]) # Player Brawler
			self.writeScID(Players["SkinID"][0], Players["SkinID"][1]) # Player Brawler Skin!
			self.writeVInt(0) # Brawler Trophies
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
		# Experience Array
		self.writeVInt(2) # Count
		self.writeVInt(0) # Normal Experience ID
		self.writeVInt(getBattleEndExp(self.device.rank)) # Normal Experience Gained
		self.writeVInt(8) # Star Player Experience ID
		self.writeVInt(10) # Star Player Experience Gained

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
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
		self.writeVInt(Milestones.MilestonesCount)  # Milestones Count (518 standart)
		self.writeHexa(Milestones.MilestonesHex)
=======
		Milestones.MilestonesArray(self)
		self.player.trophies += trophies
		db.replaceValue("trophies", self.player.trophies)
		self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] += getBattleEndTrophies(self.plrs["BattleEndType"],  self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"])
		if self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] > self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"]:
			self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"] = self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"]
		db.replaceValue("unlocked_brawlers", self.player.unlocked_brawlers)
		self.player.player_experience += getBattleEndExp(self.plrs["BattleRank"]) + 10
		db.replaceValue("player_experience", self.player.player_experience)
		self.player.gold += getBattleEndCoins(self.plrs["BattleEndType"])
		db.replaceValue("gold", self.player.gold)
		self.player.coins_reward = getBattleEndCoins(self.plrs["BattleEndType"])
		db.replaceValue("coins_reward", self.player.coins_reward)
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
		
		
class BattleEndTrio(Writer):

	def __init__(self, device, player):
		self.id = 23456
		self.device = device
		self.player = player
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
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
                              return 10
		
		IsMatchmakeBoolean = True
		
		if self.device.BattleResult in [0, 2]:
			if IsMatchmakeBoolean == False:
				IsStarPlayer = 1
			else:
				IsStarPlayer = 5
		else:
			if IsMatchmakeBoolean == False:
				IsStarPlayer = 1
			else:
				IsStarPlayer = 1
=======
				return 10
		db = DataBase(self.player)
		trophies = getBattleEndTrophies(self.plrs["BattleRank"], self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"])
		if self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] + trophies > self.brawlersTrophies:
			trophies = self.brawlersTrophies - self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] 
		
		
		
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
        # Star Player State End
		
		self.writeVInt(1) # Battle End Game Mode (5 = Showdown. Else is 3vs3)
		self.writeVInt(0) # Related To Coins Gained. If the Value is 1+, "All Coins collected"
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
		self.writeVInt(getBattleEndCoins(self.device.BattleResult)) # Coins Gained
		self.writeBool(True) # "All Coins collected" if False
		self.writeVInt(0) # First Win Coins Gained
		self.writeBool(False) # "All event experience collected" if True
		self.writeVInt(self.device.BattleResult) # Result (Victory/Defeat/Draw/Rank Score)
		self.writeVInt(getBattleEndTrophies(self.device.BattleResult)) # Trophies Result
		self.writeScID(28, 0)  # Player Profile Icon
		self.writeVInt(2) # Battle Result Type
=======
		self.writeVInt(getBattleEndCoins(self.plrs["BattleEndType"])) # Coins Gained
		self.writeVInt(6969) # "All Coins collected" if 0, its basically coins left
		self.writeVInt(0) # First Win Coins Gained
		self.writeBool(False) # "All event experience collected" if True
		self.writeVInt(self.plrs["BattleEndType"]) # Result (Victory/Defeat/Draw/Rank Score)
		self.writeVInt(trophies) # Trophies Result
		self.writeScID(28, self.player.profile_icon)  # Player Profile Icon
		self.writeBoolean(False) # is tutorial game
		self.writeBoolean(True) # is in real game
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
		self.writeVInt(0) # Coin Booster %
		self.writeVInt(0) # Coin Booster Coins Gained
		self.writeVInt(0) # Coin Doubler Coins Gained
		
		# Players Array
		self.writeVInt(6)#self.device.BattlePlayers) # Battle End Screen Players
		
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
		## you
		
		self.writeString("NostalgicBrawl") # Player Name
		self.writeVint(IsStarPlayer) # Player Team and Star Player Type
		self.writeScID(16, self.device.brawler) # Player Brawler
		if self.device.skin == 0:
			self.writeVint(0) # Player Skin
		else:
			self.writeScId(29, self.device.skin_id) # Player Skin
		self.writeVInt(1) # Brawler Trophies
		
		BotName = [self.device.Bot1Name, self.device.Bot2Name, self.device.Bot3Name, self.device.Bot4Name, self.device.Bot5Name, self.device.Bot6Name, self.device.Bot7Name, self.device.Bot8Name, self.device.Bot9Name]
		BotTeam = [self.device.Bot1Team, self.device.Bot2Team, self.device.Bot3Team, self.device.Bot4Team, self.device.Bot5Team, self.device.Bot6Team, self.device.Bot7Team, self.device.Bot8Team, self.device.Bot9Team]
		BotBrawler = [self.device.Bot1Brawler, self.device.Bot2Brawler, self.device.Bot3Brawler, self.device.Bot4Brawler, self.device.Bot5Brawler, self.device.Bot6Brawler, self.device.Bot7Brawler, self.device.Bot8Brawler, self.device.Bot9Brawler]
		for PlayerIndex in range(self.device.BattlePlayers - 1): # win
				
				self.writeString(BotName[PlayerIndex]) # Bot Name
				if self.device.PlayerTeam == 0: # win
					
					if BotTeam[PlayerIndex] == 0:
						self.writeVint(0) # Team and Star Player Type
					else:
						self.writeVint(2) # Team and Star Player Type
				else:
					if BotTeam[PlayerIndex] == 0:
						self.writeVint(2) # Team and Star Player Type
					else:
						self.writeVint(0) # Team and Star Player Type
				self.writeScId(16, BotBrawler[PlayerIndex]) # Bot Brawler
				self.writeVint(0) # Bot Skin
				self.writeVint(0) # Brawler Trophies

=======
		self.writeVInt(self.plrs["PlayersAmount"]) # Battle End Screen Players
		for Players in self.plrs["Brawlers"]:
			self.writeString(Players["Name"]) # Player Name
			self.writeBoolean(Players["IsPlayer"]) # is player
			self.writeBoolean(Players["Team"] is not self.plrs["Brawlers"][0]["Team"]) # is ennemy?
			self.writeBoolean(Players["IsPlayer"]) # is star player
			self.writeScID(Players["CharacterID"][0], Players["CharacterID"][1]) # Player Brawler
			self.writeScID(Players["SkinID"][0], Players["SkinID"][1]) # Player Brawler Skin!
			self.writeVInt(0) # Brawler Trophies
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
		# Experience Array
		self.writeVInt(2) # Count
		self.writeVInt(0) # Normal Experience ID
		self.writeVInt(getBattleEndExp(self.device.BattleResult)) # Normal Experience Gained
		self.writeVInt(8) # Star Player Experience ID
		self.writeVInt(10) # Star Player Experience Gained

		# Rank Up and Level Up Bonus Array
		self.writeVInt(0) # Count

		# Trophies and Experience Bars Array
		self.writeVInt(2) # Count
		self.writeVInt(1) # Trophies Bar Milestone ID
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
		self.writeVInt(1) # Brawler Trophies
		self.writeVInt(1) # Brawler Trophies for Rank
=======
		self.writeVInt(self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"]) # Brawler Trophies
		self.writeVInt(self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"]) # Brawler Trophies for Rank
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
		self.writeVInt(5) # Experience Bar Milestone ID
		self.writeVInt(self.player.player_experience) # Player Experience
		self.writeVInt(self.player.player_experience) # Player Experience for Level
		self.player.trophies += trophies
		db.replaceValue("trophies", self.player.trophies)
		self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] += getBattleEndTrophies(self.plrs["BattleEndType"],  self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"])
		if self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] > self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"]:
			self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"] = self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"]
		db.replaceValue("unlocked_brawlers", self.player.unlocked_brawlers)
		self.player.player_experience += getBattleEndExp(self.plrs["BattleRank"]) + 10
		db.replaceValue("player_experience", self.player.player_experience)
		self.player.gold += getBattleEndCoins(self.plrs["BattleEndType"])
		db.replaceValue("gold", self.player.gold)
		self.player.coins_reward = getBattleEndCoins(self.plrs["BattleEndType"])
		db.replaceValue("coins_reward", self.player.coins_reward)
		# Milestones Array
		self.writeBool(True) # Bool
		self.writeVInt(Milestones.MilestonesCount)  # Milestones Count (518 standart)
		self.writeHexa(Milestones.MilestonesHex)