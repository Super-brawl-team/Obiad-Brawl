from Utils.Writer import Writer
from Files.CsvLogic.Cards import Cards
import json

class LeaderboardMessage(Writer):
	def __init__(self, device, player, target):
		super().__init__(device)
		self.device = device
		self.player = player
		self.target = target
		self.id = 24403

	def encode(self):
		Brawlers228 = Cards().getBrawlers()
		self.settings = json.load(open('Settings.json'))
		self.maximumRank = self.settings["MaximumRank"]
		self.requiredTrophiesForRank = ProgressStart = [0,10,20,30,40,60,80,100,120,140,160,180,220,260,300,340,380,420,460,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200]
		if self.maximumRank <= 34:
			self.brawlersTrophies = self.requiredTrophiesForRank[self.maximumRank-1] 
		else:
			self.brawlersTrophies = self.requiredTrophiesForRank[33] + (50* (self.maximumRank-34))
	
		self.writeVInt(self.device.LeaderboardInfo)
		if self.device.LeaderboardInfo == 1: 
			self.writeVInt(0)
		else: 
			self.writeDataReference(int(self.target[0]), int(self.target[1]))
		if self.device.LeaderboardType == 0:
			self.writeString()
		else:
			self.writeString(self.player.region)

		if self.device.LeaderboardInfo == 1: # Players LeaderBoard case ?
			self.writeVInt(1) # Players Count
			self.writeLogicLong(0, 1) # ID
			self.writeVInt(1)
			self.writeVInt(self.brawlersTrophies * len(Brawlers228)) # Player Trophies
			self.writeVInt(1)
			self.writeString(self.player.name)  # Player Name
			self.writeString("Primo Team") # Club Name
			self.writeVInt(500) # Player Level
			self.writeScID(28, 0) # Player Icon
			self.writeVInt(0)

		elif self.device.LeaderboardInfo == 0: #Brawlers LeaderBoard case?
			self.writeVInt(1) # Players Count
			self.writeLogicLong(0, 1) # ID
			self.writeVInt(1)
			self.writeVInt(self.brawlersTrophies) # Player Trophies
			self.writeVInt(1)
			self.writeString(self.player.name)  # Player Name
			self.writeString("Primo Team") # Club Name
			self.writeVInt(500) # Player Level
			self.writeScID(28, 0) # Player Icon
			self.writeVInt(0)

		elif self.device.LeaderboardInfo == 2: #Club leaderboard case
			self.writeVInt(1) # Clubs Count
			self.writeLogicLong(0, 1) # ID
			self.writeVInt(1)
			self.writeVInt(self.brawlersTrophies  * len(Brawlers228)) # Club Trophies
			self.writeVInt(2)
			self.writeString("Primo Team") # Club Name
			self.writeVInt(1) # Club Members Count
			self.writeVInt(8) # Club Badge
			self.writeVInt(19) # Club Name Color
		
		self.writeVInt(0)
		self.writeVInt(0)
		self.writeVInt(0)
		self.writeVInt(0)
		self.writeString(self.player.region) #Region

