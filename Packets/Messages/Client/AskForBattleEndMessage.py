# sroyzi team presents you... supershitcode
from Packets.Messages.Server.BattleEnd import *
from Logic.Player import Player
from Utils.Reader import ByteStream


class AskForBattleEnd(ByteStream):

	def __init__(self, data, device):
		super().__init__(data)
		self.device = device

	def decode(self):
		self.device.BattleResult = self.ReadVint()
		self.ReadVint()
		self.device.rank = self.ReadVint()
		self.ReadVint() # location csvid
		self.ReadVint() # map
		self.BattlePlayers = self.read_Vint() # Battle End Players
		self.read_Vint() # Brawler CsvID
		self.device.brawler = self.read_Vint() # Selected Brawler
		self.Skin = self.read_Vint() # Skin CsvID
		if self.Skin == 0:
			pass
		else:
			self.device.skin_id = self.read_Vint() # Selected Skin
		self.PlayerTeam = self.read_Vint()
		self.IsPlayer = self.read_Vint()
		self.device.PName = self.readString()
		
	# bots start
		
		self.read_Vint()
		self.Bot1Brawler = self.read_Vint() #bot brawler
		self.Bot1Skin = self.read_Vint()
		self.Bot1Team = self.read_Vint()  #red or blue
		self.Bot1IsPlayer = self.read_Vint()
		self.Bot1Name = self.read_string()
		
		
		self.read_Vint()
		self.Bot2Brawler = self.read_Vint() #bot brawler
		self.Bot2Skin = self.read_Vint()
		self.Bot2Team = self.read_Vint()  #red or blue
		self.Bot2IsPlayer = self.read_Vint()
		self.Bot2Name = self.read_string()
		
		
		self.read_Vint()
		self.Bot3Brawler = self.read_Vint() #bot brawler
		self.Bot3Skin = self.read_Vint()
		self.Bot3Team = self.read_Vint()  #red or blue
		self.Bot3IsPlayer = self.read_Vint()
		self.Bot3Name = self.read_string()
		
		
		self.read_Vint()
		self.Bot4Brawler = self.read_Vint() #bot brawler
		self.Bot4Skin = self.read_Vint()
		self.Bot4Team = self.read_Vint()  #red or blue
		self.Bot4IsPlayer = self.read_Vint()
		self.Bot4Name = self.read_string()
		
		
		self.read_Vint()
		self.Bot5Brawler = self.read_Vint() #bot brawler
		self.Bot5Skin = self.read_Vint()
		self.Bot5Team = self.read_Vint()  #red or blue
		self.Bot5IsPlayer = self.read_Vint()
		self.Bot5Name = self.read_string()
		
		
		self.read_Vint()
		self.Bot6Brawler = self.read_Vint() #bot brawler
		self.Bot6Skin = self.read_Vint()
		self.Bot6Team = self.read_Vint()  #red or blue
		self.Bot6IsPlayer = self.read_Vint()
		self.Bot6Name = self.read_string()
		
		
		self.read_Vint()
		self.Bot7Brawler = self.read_Vint() #bot brawler
		self.Bot7Skin = self.read_Vint()
		self.Bot7Team = self.read_Vint()  #red or blue
		self.Bot7IsPlayer = self.read_Vint()
		self.Bot7Name = self.read_string()
		
		
		self.read_Vint()
		self.Bot8Brawler = self.read_Vint() #bot brawler
		self.Bot8Skin = self.read_Vint()
		self.Bot8Team = self.read_Vint()  #red or blue
		self.Bot8IsPlayer = self.read_Vint()
		self.Bot8Name = self.read_string()
		
		
		self.read_Vint()
		self.Bot9Brawler = self.read_Vint() #bot brawler
		self.Bot9Skin = self.read_Vint()
		self.Bot9Team = self.read_Vint()  #red or blue
		self.Bot9IsPlayer = self.read_Vint()
		self.Bot9Name = self.read_string()
	# bots end
		

	def process(self):
		if self.device.rank != 0: # showdown
			BattleEndSD(self.device, self.device.Player).Send()
		else:
			if self.device.team == 0:
				self.device.Bot1Name = self.Bot1Name
				self.device.Bot2Name = self.Bot2Name
				self.device.Bot3Name = self.Bot3Name
				self.device.Bot4Name = self.Bot4Name
				self.device.Bot5Name = self.Bot5Name
				self.device.Bot6Name = self.Bot6Name
				self.device.Bot7Name = self.Bot7Name
				self.device.Bot8Name = self.Bot8Name
				self.device.Bot9Name = self.Bot9Name
				self.device.Bot1Brawler = self.Bot1Brawler
				self.device.Bot2Brawler = self.Bot2Brawler
				self.device.Bot3Brawler = self.Bot3Brawler
				self.device.Bot4Brawler = self.Bot4Brawler
				self.device.Bot5Brawler = self.Bot5Brawler
				self.device.Bot6Brawler = self.Bot6Brawler
				self.device.Bot7Brawler = self.Bot7Brawler
				self.device.Bot8Brawler = self.Bot8Brawler
				self.device.Bot9Brawler = self.Bot9Brawler
				self.device.PlayerTeam = self.PlayerTeam
				self.device.Bot1Team = self.Bot1Team
				self.device.Bot2Team = self.Bot2Team
				self.device.Bot3Team = self.Bot3Team
				self.device.Bot4Team = self.Bot4Team
				self.device.Bot5Team = self.Bot5Team
				self.device.Bot6Team = self.Bot6Team
				self.device.Bot7Team = self.Bot7Team
				self.device.Bot8Team = self.Bot8Team
				self.device.Bot9Team = self.Bot9Team
				self.device.BattlePlayers = self.BattlePlayers
				BattleEndTrio(self.device, self.device.Player).Send()
			else:
				self.device.Bot1Name = self.Bot1Name
				self.device.Bot2Name = self.Bot2Name
				self.device.Bot3Name = self.Bot3Name
				self.device.Bot4Name = self.Bot4Name
				self.device.Bot5Name = self.Bot5Name
				self.device.Bot6Name = self.Bot6Name
				self.device.Bot7Name = self.Bot7Name
				self.device.Bot8Name = self.Bot8Name
				self.device.Bot9Name = self.Bot9Name
				self.device.Bot1Brawler = self.Bot1Brawler
				self.device.Bot2Brawler = self.Bot2Brawler
				self.device.Bot3Brawler = self.Bot3Brawler
				self.device.Bot4Brawler = self.Bot4Brawler
				self.device.Bot5Brawler = self.Bot5Brawler
				self.device.Bot6Brawler = self.Bot6Brawler
				self.device.Bot7Brawler = self.Bot7Brawler
				self.device.Bot8Brawler = self.Bot8Brawler
				self.device.Bot9Brawler = self.Bot9Brawler
				self.device.PlayerTeam = self.PlayerTeam
				self.device.Bot1Team = self.Bot1Team
				self.device.Bot2Team = self.Bot2Team
				self.device.Bot3Team = self.Bot3Team
				self.device.Bot4Team = self.Bot4Team
				self.device.Bot5Team = self.Bot5Team
				self.device.Bot6Team = self.Bot6Team
				self.device.Bot7Team = self.Bot7Team
				self.device.Bot8Team = self.Bot8Team
				self.device.Bot9Team = self.Bot9Team
				self.device.BattlePlayers = self.BattlePlayers
				BattleEndTrio(self.device, self.device.Player).Send()