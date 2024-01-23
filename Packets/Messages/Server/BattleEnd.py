from Utils.Writer import Writer
from Logic.Milestones import Milestones


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
		self.writeVInt(0) # Coin Booster %
		self.writeVInt(0) # Coin Booster Coins Gained
		self.writeVInt(0) # Coin Doubler Coins Gained
		
		# Players Array
		self.writeVInt(self.plrs["PlayersAmount"]) # Battle End Screen Players
		for Players in self.plrs["Brawlers"]:
			self.writeString(Players["Name"]) # Player Name
			self.writeVInt(IsStarPlayer) # team
			self.writeScID(Players["CharacterID"][0], Players["CharacterID"][1]) # Player Brawler
			self.writeScID(Players["SkinID"][0], Players["SkinID"][1]) # Player Brawler Skin!
			self.writeVInt(0) # Brawler Trophies
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
		Milestones.MilestonesArray(self)
		
		
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
        # Star Player State End
		
		self.writeVInt(1) # Battle End Game Mode (5 = Showdown. Else is 3vs3)
		self.writeVInt(0) # Related To Coins Gained. If the Value is 1+, "All Coins collected"
		self.writeVInt(getBattleEndCoins(self.plrs["BattleEndType"])) # Coins Gained
		self.writeBool(True) # "All Coins collected" if False
		self.writeVInt(0) # First Win Coins Gained
		self.writeBool(False) # "All event experience collected" if True
		self.writeVInt(self.plrs["BattleEndType"]) # Result (Victory/Defeat/Draw/Rank Score)
		self.writeVInt(getBattleEndTrophies(self.plrs["BattleEndType"])) # Trophies Result
		self.writeScID(28, 0)  # Player Profile Icon
		self.writeVInt(2) # Battle Result Type
		self.writeVInt(0) # Coin Booster %
		self.writeVInt(0) # Coin Booster Coins Gained
		self.writeVInt(0) # Coin Doubler Coins Gained
		
		# Players Array
		self.writeVInt(self.plrs["PlayersAmount"]) # Battle End Screen Players
		for Players in self.plrs["Brawlers"]:
			self.writeString(Players["Name"]) # Player Name
			self.writeVInt(IsStarPlayer) # isStarPlayer but its only you hehe
			self.writeScID(Players["CharacterID"][0], Players["CharacterID"][1]) # Player Brawler
			self.writeScID(Players["SkinID"][0], Players["SkinID"][1]) # Player Brawler Skin!
			self.writeVInt(0) # Brawler Trophies
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
		Milestones.MilestonesArray(self)
		