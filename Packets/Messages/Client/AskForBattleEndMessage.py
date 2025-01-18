from Packets.Messages.Server.BattleEndMessage import *
from Logic.Player import Player
from Utils.Reader import ByteStream


class AskForBattleEndMessage(ByteStream):

	def __init__(self, data, device, player):
		super().__init__(data)
		self.device = device
		self.data = data
		self.player = player

	def decode(self):
		self.plrs = {}
		self.plrs["BattleEndType"] = self.readVInt() # battle result
		self.plrs["BattleTime"] = self.readVInt() # time played ?
	
		self.plrs["BattleRank"] = self.readVInt() # rank so basically is won/lose/draw for 3v3 and the rank for sd
		self.plrs["CsvID0"] = self.readVInt()
		self.plrs["Location"] = self.readVInt() # location or the map if you prefer
		self.plrs["PlayersAmount"] = self.readVInt() # Battle End Players
		self.plrs["Brawlers"] = []
		for x in range(self.plrs["PlayersAmount"]):
		# HeroDataEntry::encode
			self.plrs["Brawlers"].append({
				"CharacterID": self.readDataReference(),
				"SkinID": self.readDataReference(),
				"Team": self.readVInt(),
				"IsPlayer": self.readBoolean(), 
				"Name": self.readString()
			})
	def process(self):
		
		if self.plrs["BattleRank"] != 0: # showdown
			BattleEndSD(self.device, self.player, self.plrs).Send()
		else:
			BattleEndTrio(self.device, self.player, self.plrs).Send()