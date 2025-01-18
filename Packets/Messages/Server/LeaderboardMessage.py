from Utils.Writer import Writer
from Files.CsvLogic.Cards import Cards
import json
from Database.DatabaseManager import DataBase

class LeaderboardMessage(Writer):
	def __init__(self, device, player, fields):
		super().__init__(device)
		self.device = device
		self.player = player
		self.fields = fields
		self.id = 24403

	def encode(self):
		db = DataBase(self.player)
		
		self.indexOfPlayer = 1
		self.writeVInt(self.fields["leaderboardType"])
		if self.fields["leaderboardType"] == 0:
			self.writeDataReference(16, self.fields["targetBrawler"][1]) # SCID
		else:
			self.writeVInt(0)
		self.writeString(self.player.region if self.fields["isLocal"] else None)

		self.writeVInt(len(self.fields["entries"])) # Players Count

		for entry in self.fields["entries"]:
			self.writeVInt(0) # High ID
			self.writeVInt(entry["clubID"] if self.fields["leaderboardType"] == 2 else entry["low_id"]) # Low ID
			self.writeVInt(1)
			self.writeVInt(entry['trophies'] if self.fields["leaderboardType"] != 0 else entry['unlocked_brawlers'][str(self.fields["targetBrawler"][1])]["Trophies"]) # Player Trophies
			isPlayer = self.fields["leaderboardType"] != 2
			self.writeBoolean(isPlayer)
			if isPlayer:
				club = db.loadClub(entry["club_id"])
				if ["low_id"] == self.player.low_id:
					self.indexOfPlayer = self.fields["entries"].index(entry) + 1
				self.writeString(entry['name'])
				self.writeString(club["info"]["name"] if entry["club_id"] != 0 else "")
				self.writeVInt(entry['player_experience'])
				self.writeDataReference(28, entry['profile_icon'])
			isClub = not isPlayer
			self.writeBoolean(isClub)
			if isClub:
				self.writeString(entry["name"]) # Club Name
				self.writeVInt(len(entry["memberCount"])) # Club Members Count
				self.writeDataReference(8, entry["clubBadge"]) # Club Badge


		self.writeVint(0)
		self.writeVint(self.indexOfPlayer)
		self.writeVint(0)
		self.writeVint(0) # Leaderboard Region
		self.writeString(self.player.region)