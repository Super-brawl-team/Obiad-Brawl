from Utils.Writer import Writer
<<<<<<< HEAD
=======
<<<<<<<< HEAD:Packets/Messages/Server/BattleEnd.py
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
from Logic import Milestones
========
from Logic.Milestones import Milestones
>>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b:Packets/Messages/Server/BattleEndMessage.py


=======
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
from Logic.Milestones import Milestones
<<<<<<< Updated upstream


=======
from Database.DatabaseManager import DataBase
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters
import json
<<<<<<< HEAD
=======
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
class BattleEndSD(Writer):

	def __init__(self, device, player, plrs):
		self.id = 23456
		self.device = device
		self.plrs = plrs
		self.player = player
		super().__init__(self.device)

	def encode(self):
		def getBattleEndTrophies(rang):
			if rang == 10:
				return 0
			elif rang == 9:
				return 1
			elif rang == 8:
				return 2
			elif rang == 7:
				return 3
			elif rang == 6:
				return 4
			elif rang == 5:
				return 5
			elif rang == 4:
				return 5
			elif rang == 3:
				return 6
			elif rang == 2:
				return 7
			elif rang == 1:
				return 8
		
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
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
=======
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
>>>>>>> Stashed changes
		
		IsMatchmakeBoolean = True
		
		if self.plrs["BattleEndType"] in [0, 2]:
			if IsMatchmakeBoolean == False:
				IsStarPlayer = 1
			else:
				IsStarPlayer = 5
		else:
			if IsMatchmakeBoolean == False:
				IsStarPlayer = 1
			else:
				IsStarPlayer = 1
		
<<<<<<< Updated upstream
=======
		self.writeVInt(5) # Battle End Game Mode (5 = Showdown. Else is 3vs3)
		self.writeVInt(0) # Related To Coins Gained. If the Value is 1+, "All Coins collected"
		self.writeVInt(getBattleEndCoins(self.plrs["BattleRank"])) # Coins Gained
		self.writeBool(True) # "All Coins collected" if False
		self.writeVInt(0) # First Win Coins Gained
		self.writeBool(False) # "All event experience collected" if True
		self.writeVInt(self.plrs["BattleRank"]) # Result (Victory/Defeat/Draw/Rank Score)
		self.writeVInt(getBattleEndTrophies(self.plrs["BattleRank"])) # Trophies Result
		self.writeScID(28, 0)  # Player Profile Icon
		self.writeVInt(2) # Battle Result Type
=======
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
		db = DataBase(self.player)
		trophies = getBattleEndTrophies(self.plrs["BattleRank"], self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"])
		if self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] + trophies > self.brawlersTrophies:
			trophies = self.brawlersTrophies - self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"] 
>>>>>>> Stashed changes
		self.writeVInt(5) # Battle End Game Mode (5 = Showdown. Else is 3vs3)
		self.writeVInt(0) # Related To Coins Gained. If the Value is 1+, "All Coins collected"
		self.writeVInt(getBattleEndCoins(self.plrs["BattleRank"])) # Coins Gained
		self.writeBool(True) # "All Coins collected" if False
		self.writeVInt(0) # First Win Coins Gained
		self.writeBool(False) # "All event experience collected" if True
		self.writeVInt(self.plrs["BattleRank"]) # Result (Victory/Defeat/Draw/Rank Score)
<<<<<<< Updated upstream
		self.writeVInt(getBattleEndTrophies(self.plrs["BattleRank"])) # Trophies Result
		self.writeScID(28, 0)  # Player Profile Icon
		self.writeVInt(2) # Battle Result Type
=======
		
		self.writeVInt(trophies) # Trophies Result
		self.writeScID(28, self.player.profile_icon)  # Player Profile Icon
		self.writeBoolean(False) # is tutorial game
		self.writeBoolean(True) # is in real game
<<<<<<< HEAD
=======
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
		self.writeVInt(0) # Coin Booster %
		self.writeVInt(0) # Coin Booster Coins Gained
		self.writeVInt(0) # Coin Doubler Coins Gained
		
		# Players Array
<<<<<<< HEAD
=======
<<<<<<<< HEAD:Packets/Messages/Server/BattleEnd.py
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
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
		self.writeVInt(self.plrs["PlayersAmount"]) # Battle End Screen Players
		for Players in self.plrs["Brawlers"]:
			self.writeString(Players["Name"]) # Player Name
			if Players["Name"] == self.player.name:
				self.writeVInt(IsStarPlayer) # team
			else:
				if Players["Team"] == 0:
					self.writeVInt(0)
				else:
					self.writeVInt(2)
			self.writeScID(Players["CharacterID"][0], Players["CharacterID"][1]) # Player Brawler
			self.writeScID(Players["SkinID"][0], Players["SkinID"][1]) # Player Brawler Skin!
			self.writeVInt(0) # Brawler Trophies
<<<<<<< HEAD
=======
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
========
		self.writeVInt(self.plrs["PlayersAmount"]) # Battle End Screen Players
		for Players in self.plrs["Brawlers"]:
			self.writeString(Players["Name"]) # Player Name
			if Players["Name"] == self.player.name:
				self.writeVInt(IsStarPlayer) # team
			else:
				if Players["Team"] == 0:
					self.writeVInt(0)
				else:
					self.writeVInt(2)
			self.writeScID(Players["CharacterID"][0], Players["CharacterID"][1]) # Player Brawler
			self.writeScID(Players["SkinID"][0], Players["SkinID"][1]) # Player Brawler Skin!
			self.writeVInt(0) # Brawler Trophies
>>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b:Packets/Messages/Server/BattleEndMessage.py
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
		# Experience Array
		self.writeVInt(2) # Count
		self.writeVInt(0) # Normal Experience ID
		self.writeVInt(getBattleEndExp(self.plrs["BattleRank"])) # Normal Experience Gained
		self.writeVInt(8) # Star Player Experience ID
		self.writeVInt(10) # Star Player Experience Gained

		# Rank Up and Level Up Bonus Array
		self.writeVInt(0) # Count

		# Trophies and Experience Bars Array
		self.writeVInt(2) # Count
		self.writeVInt(1) # Trophies Bar Milestone ID
		self.writeVInt(0) # Brawler Trophies
		self.writeVInt(0) # Brawler Trophies for Rank
		self.writeVInt(5) # Experience Bar Milestone ID
		self.writeVInt(0) # Player Experience
		self.writeVInt(0) # Player Experience for Level
		
		# Milestones Array
		self.writeBool(True) # Bool
<<<<<<< HEAD
=======
<<<<<<<< HEAD:Packets/Messages/Server/BattleEnd.py
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
		self.writeVInt(Milestones.MilestonesCount)  # Milestones Count (518 standart)
		self.writeHexa(Milestones.MilestonesHex)
=======
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
		Milestones.MilestonesArray(self)
<<<<<<< Updated upstream
=======
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
<<<<<<< HEAD
=======
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
========
		Milestones.MilestonesArray(self)
>>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b:Packets/Messages/Server/BattleEndMessage.py
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
		
		
class BattleEndTrio(Writer):

	def __init__(self, device, player, plrs):
		self.id = 23456
		self.device = device
		self.plrs = plrs
		self.player = player
		super().__init__(self.device)

	def encode(self):
		def getBattleEndTrophies(rang):
			if rang == 0: # win
				return 5
			else:
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
<<<<<<< HEAD
=======
<<<<<<<< HEAD:Packets/Messages/Server/BattleEnd.py
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
                              return 10
========
				return 10
>>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b:Packets/Messages/Server/BattleEndMessage.py
		
		IsMatchmakeBoolean = True
		
		if self.plrs["BattleEndType"] in [0, 2]:
			if IsMatchmakeBoolean == False:
				IsStarPlayer = 1
			else:
				IsStarPlayer = 5
		else:
			if IsMatchmakeBoolean == False:
				IsStarPlayer = 1
			else:
				IsStarPlayer = 1
<<<<<<<< HEAD:Packets/Messages/Server/BattleEnd.py
=======
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
				return 10
		
		IsMatchmakeBoolean = True
		
		if self.plrs["BattleEndType"] in [0, 2]:
			if IsMatchmakeBoolean == False:
				IsStarPlayer = 1
			else:
				IsStarPlayer = 5
		else:
			if IsMatchmakeBoolean == False:
				IsStarPlayer = 1
			else:
				IsStarPlayer = 1
		
		
<<<<<<< HEAD
=======
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
========
		
		
>>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b:Packets/Messages/Server/BattleEndMessage.py
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
        # Star Player State End
		
		self.writeVInt(1) # Battle End Game Mode (5 = Showdown. Else is 3vs3)
		self.writeVInt(0) # Related To Coins Gained. If the Value is 1+, "All Coins collected"
<<<<<<< HEAD
=======
<<<<<<<< HEAD:Packets/Messages/Server/BattleEnd.py
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
		self.writeVInt(getBattleEndCoins(self.device.BattleResult)) # Coins Gained
========
		self.writeVInt(getBattleEndCoins(self.plrs["BattleEndType"])) # Coins Gained
>>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b:Packets/Messages/Server/BattleEndMessage.py
		self.writeBool(True) # "All Coins collected" if False
		self.writeVInt(0) # First Win Coins Gained
		self.writeBool(False) # "All event experience collected" if True
		self.writeVInt(self.plrs["BattleEndType"]) # Result (Victory/Defeat/Draw/Rank Score)
		self.writeVInt(getBattleEndTrophies(self.plrs["BattleEndType"])) # Trophies Result
		self.writeScID(28, 0)  # Player Profile Icon
		self.writeVInt(2) # Battle Result Type
=======
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
		self.writeVInt(getBattleEndCoins(self.plrs["BattleEndType"])) # Coins Gained
		self.writeBool(True) # "All Coins collected" if False
		self.writeVInt(0) # First Win Coins Gained
		self.writeBool(False) # "All event experience collected" if True
		self.writeVInt(self.plrs["BattleEndType"]) # Result (Victory/Defeat/Draw/Rank Score)
<<<<<<< Updated upstream
		self.writeVInt(getBattleEndTrophies(self.plrs["BattleEndType"])) # Trophies Result
		self.writeScID(28, 0)  # Player Profile Icon
		self.writeVInt(2) # Battle Result Type
=======
		self.writeVInt(trophies) # Trophies Result
		self.writeScID(28, self.player.profile_icon)  # Player Profile Icon
		self.writeBoolean(False) # is tutorial game
		self.writeBoolean(True) # is in real game
<<<<<<< HEAD
=======
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
		self.writeVInt(0) # Coin Booster %
		self.writeVInt(0) # Coin Booster Coins Gained
		self.writeVInt(0) # Coin Doubler Coins Gained
		
		# Players Array
		
<<<<<<< HEAD
=======
<<<<<<<< HEAD:Packets/Messages/Server/BattleEnd.py
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
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
		self.writeVInt(self.plrs["PlayersAmount"]) # Battle End Screen Players
		for Players in self.plrs["Brawlers"]:
			self.writeString(Players["Name"]) # Player Name
			if Players["Name"] == self.player.name:
				self.writeVInt(IsStarPlayer) # team
			else:
				if Players["Team"] == 0:
					self.writeVInt(0)
				else:
					self.writeVInt(2)
			self.writeScID(Players["CharacterID"][0], Players["CharacterID"][1]) # Player Brawler
			self.writeScID(Players["SkinID"][0], Players["SkinID"][1]) # Player Brawler Skin!
			self.writeVInt(0) # Brawler Trophies
<<<<<<< HEAD
=======
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
========
		self.writeVInt(self.plrs["PlayersAmount"]) # Battle End Screen Players
		for Players in self.plrs["Brawlers"]:
			self.writeString(Players["Name"]) # Player Name
			if Players["Name"] == self.player.name:
				self.writeVInt(IsStarPlayer) # team
			else:
				if Players["Team"] == 0:
					self.writeVInt(0)
				else:
					self.writeVInt(2)
			self.writeScID(Players["CharacterID"][0], Players["CharacterID"][1]) # Player Brawler
			self.writeScID(Players["SkinID"][0], Players["SkinID"][1]) # Player Brawler Skin!
			self.writeVInt(0) # Brawler Trophies
>>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b:Packets/Messages/Server/BattleEndMessage.py
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
		# Experience Array
		self.writeVInt(2) # Count
		self.writeVInt(0) # Normal Experience ID
		self.writeVInt(getBattleEndExp(self.plrs["BattleRank"])) # Normal Experience Gained
		self.writeVInt(8) # Star Player Experience ID
		self.writeVInt(10) # Star Player Experience Gained

		# Rank Up and Level Up Bonus Array
		self.writeVInt(0) # Count

		# Trophies and Experience Bars Array
		self.writeVInt(2) # Count
		self.writeVInt(1) # Trophies Bar Milestone ID
<<<<<<< Updated upstream
		self.writeVInt(0) # Brawler Trophies
		self.writeVInt(0) # Brawler Trophies for Rank
=======
<<<<<<< HEAD
		self.writeVInt(self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"]) # Brawler Trophies
		self.writeVInt(self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"]) # Brawler Trophies for Rank
=======
<<<<<<<< HEAD:Packets/Messages/Server/BattleEnd.py
<<<<<<< Updated upstream:Packets/Messages/Server/BattleEnd.py
		self.writeVInt(1) # Brawler Trophies
		self.writeVInt(1) # Brawler Trophies for Rank
=======
		self.writeVInt(self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["Trophies"]) # Brawler Trophies
		self.writeVInt(self.player.unlocked_brawlers[str(self.plrs["Brawlers"][0]["CharacterID"][1])]["HighestTrophies"]) # Brawler Trophies for Rank
>>>>>>> Stashed changes:Packets/Messages/Server/BattleEndMessage.py
========
		self.writeVInt(0) # Brawler Trophies
		self.writeVInt(0) # Brawler Trophies for Rank
>>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b:Packets/Messages/Server/BattleEndMessage.py
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
		self.writeVInt(5) # Experience Bar Milestone ID
		self.writeVInt(0) # Player Experience
		self.writeVInt(0) # Player Experience for Level
		
		# Milestones Array
		self.writeBool(True) # Bool
		Milestones.MilestonesArray(self)
		