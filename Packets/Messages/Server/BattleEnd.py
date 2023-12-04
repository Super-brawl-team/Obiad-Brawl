from Utils.Writer import Writer
from Logic import Milestones


class BattleEndSD(Writer):

	def __init__(self, device, player):
		self.id = 23456
		self.device = device
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
		self.writeVInt(0) # Coin Booster %
		self.writeVInt(0) # Coin Booster Coins Gained
		self.writeVInt(0) # Coin Doubler Coins Gained
		
		# Players Array
		self.writeVInt(1) # Battle End Screen Players
		self.writeString("NostalgicBrawl") # Player Name
		self.writeVInt(IsStarPlayer) # Player Team and Star Player Type
		self.writeScID(16, self.device.brawler) # Player Brawler
		if self.device.skin == 0:
			self.writeVint(0) # Player Skin
		else:
			self.writeScId(29, self.device.skin_id) # Player Skin
		self.writeVInt(1) # Brawler Trophies
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
		self.writeVInt(0) # Brawler Trophies
		self.writeVInt(0) # Brawler Trophies for Rank
		self.writeVInt(5) # Experience Bar Milestone ID
		self.writeVInt(0) # Player Experience
		self.writeVInt(0) # Player Experience for Level
		
		# Milestones Array
		self.writeBool(True) # Bool
		self.writeVInt(Milestones.MilestonesCount)  # Milestones Count (518 standart)
		self.writeHexa(Milestones.MilestonesHex)
		
		
class BattleEndTrio(Writer):

	def __init__(self, device, player):
		self.id = 23456
		self.device = device
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
        # Star Player State End
		
		self.writeVInt(1) # Battle End Game Mode (5 = Showdown. Else is 3vs3)
		self.writeVInt(0) # Related To Coins Gained. If the Value is 1+, "All Coins collected"
		self.writeVInt(getBattleEndCoins(self.device.BattleResult)) # Coins Gained
		self.writeBool(True) # "All Coins collected" if False
		self.writeVInt(0) # First Win Coins Gained
		self.writeBool(False) # "All event experience collected" if True
		self.writeVInt(self.device.BattleResult) # Result (Victory/Defeat/Draw/Rank Score)
		self.writeVInt(getBattleEndTrophies(self.device.BattleResult)) # Trophies Result
		self.writeScID(28, 0)  # Player Profile Icon
		self.writeVInt(2) # Battle Result Type
		self.writeVInt(0) # Coin Booster %
		self.writeVInt(0) # Coin Booster Coins Gained
		self.writeVInt(0) # Coin Doubler Coins Gained
		
		# Players Array
		self.writeVInt(6)#self.device.BattlePlayers) # Battle End Screen Players
		
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
		self.writeVInt(1) # Brawler Trophies
		self.writeVInt(1) # Brawler Trophies for Rank
		self.writeVInt(5) # Experience Bar Milestone ID
		self.writeVInt(0) # Player Experience
		self.writeVInt(0) # Player Experience for Level
		
		# Milestones Array
		self.writeBool(True) # Bool
		self.writeVInt(Milestones.MilestonesCount)  # Milestones Count (518 standart)
		self.writeHexa(Milestones.MilestonesHex)