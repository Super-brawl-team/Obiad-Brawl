from Packets.Messages.Server.BattleEndMessage import *
from Logic.Player import Player
from Utils.Writer import Writer


class ForceSendBattleEnd(Writer):

	def __init__(self, device, player):
		super().__init__(device)
		self.device = device
		self.player = player

	def decode(self):
		self.plrs = {}
		self.plrs["BattleEndType"] = 5 # battle result
		self.plrs["BattleTime"] = 1 # time played ?
	
		self.plrs["BattleRank"] = 1 # rank so basically is won/lose/draw for 3v3 and the rank for sd
		self.plrs["CsvID0"] = 15
		self.plrs["Location"] = 0 # location or the map if you prefer
		self.plrs["PlayersAmount"] = 10 # Battle End Players
		self.plrs["Brawlers"] = []
		for x in range(self.plrs["PlayersAmount"]):
		# HeroDataEntry::encode
			if x != 0:
				team = 2
				isPlayer = False
				Name = f"Bot {x}"
			else:
				team = 1
				isPlayer = True
				Name = self.player.name
			self.plrs["Brawlers"].append({
				"CharacterID": [16, 0],
				"SkinID": [29, 0],
				"Team": team,
				"IsPlayer": isPlayer, 
				"Name": Name
			})
		self.plrs["isInRealGame"] = False
	def process(self):
		
		if self.plrs["BattleRank"] != 0: # showdown
			BattleEndSD(self.device, self.player, self.plrs).Send()
		else:
			BattleEndTrio(self.device, self.player, self.plrs).Send()