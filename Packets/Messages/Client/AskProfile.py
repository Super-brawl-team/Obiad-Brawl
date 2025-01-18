# -*- coding: utf-8 -*-

from Packets.Messages.Server.Profile import Profile
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase

class AskProfile(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.HighID = self.readInt()
        self.LowID = self.readInt()

    def process(self):
        db = DataBase(self.player)
        self.players = db.getAllPlayers()
        Profile(self.device, self.player, self.HighID, self.LowID, self.players).Send()
