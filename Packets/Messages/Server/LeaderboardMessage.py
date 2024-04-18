from Utils.Writer import Writer
from Files.CsvLogic.Cards import Cards

class LeaderboardMessage(Writer):
	def __init__(self, device):
		super().__init__(device)
		self.device = device
		self.id = 24403

	def encode(self):
		Brawlers228 = Cards().getBrawlers()
		self.writeVInt(1)#self.device.LeaderboardInfo)
		self.writeVInt(0)

		if self.device.LeaderboardType == 0:
			self.writeString()
		else:
			self.writeString("FR")

		if self.device.LeaderboardInfo == 0: # Players LeaderBoard case ?
			self.writeVInt(1) # Players Count
			self.writeLogicLong(0, 1) # ID
			self.writeVInt(1)
			self.writeVInt(500 * len(Brawlers228)) # Player Trophies
			self.writeVInt(1)
			self.writeString(self.player.name)  # Player Name
			self.writeString("Primo Team") # Club Name
			self.writeVInt(500) # Player Level
			self.writeScID(28, 0) # Player Icon
			self.writeVInt(0)

		elif self.device.LeaderboardInfo == 1: #Brawlers LeaderBoard case?
			self.writeVInt(1) # Players Count
			self.writeLogicLong(0, 1) # ID
			self.writeVInt(1)
			self.writeVInt(400 * len(Brawlers228)) # Player Trophies
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
			self.writeVInt(500 * len(Brawlers228)) # Club Trophies
			self.writeVInt(2)
			self.writeString("Primo Team") # Club Name
			self.writeVInt(1) # Club Members Count
			self.writeVInt(8) # Club Badge
			self.writeVInt(19) # Club Name Color
		
		self.writeVInt(0)
		self.writeVInt(0)
		self.writeVInt(0)
		self.writeVInt(0)
		self.writeString("FR") #Region

