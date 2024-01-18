# sroyzi team presents you... supershitcode
from Packets.Messages.Server.BattleEnd import *
from Logic.Player import Player
from Utils.Reader import ByteStream


class AskForBattleEnd(ByteStream):

	def __init__(self, data, device):
		super().__init__(data)
		self.device = device

	def decode(self):
		self.plrs = {}
		self.plrs["BattleEndType"] = self.ReadVint() # battle result
		self.plrs["BattleTime"] = self.ReadVint() # time played ?
		self.plrs["BattleRank"] = self.ReadVint() # rank so basically is won/lose/draw for 3v3 and the rank for sd
		self.plrs["Location"] = self.ReadVint() # location or the map if you prefer
		self.plrs["PlayersAmount"] = self.read_Vint() # Battle End Players
		for x in range(self.plrs["PlayersAmount"]):
			# HeroDataEntry::encode
			self.plrs["Brawlers"].append({"Brawlers": {"BrawlerID": self.readDataReference(), "SkinID": self.readDataReference()}, "Team": self.ReadVint(), "IsPlayer": self.ReadVint(), "Name": self.read_string()})
	def process(self):
		
		if self.plrs["BattleRank"] != 0: # showdown
			BattleEndSD(self.device, self.device.Player, self.plrs).Send()
		else:
			BattleEndTrio(self.device, self.device.Player, self.plrs).Send()