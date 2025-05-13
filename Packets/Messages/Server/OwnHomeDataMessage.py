# -*- coding: utf-8 -*-
from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
from Entries.LogicClientAvatar import LogicClientAvatar
from Entries.LogicClientHome import LogicClientHome

class OwnHomeDataMessage(Writer):

	def __init__(self, device, player):
		self.id = 24101
		self.device = device
		self.player = player
		super().__init__(self.device)

	def encode(self):
		db = DataBase(self.player)
		db.loadAccount()
		LogicClientHome.encode(self, self.player)
		LogicClientAvatar.encode(self, self.player)
		self.writeVInt(2017189) # dudka timestamps from hell
		self.player.player_status = 2
		db.replaceValue("player_status", self.player.player_status)