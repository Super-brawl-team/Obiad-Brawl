# -*- coding: utf-8 -*-

from Packets.Messages.Server.Profile import Profile
from Utils.Reader import ByteStream
from Logic.Player import Player
from Database.DatabaseManager import DataBase

class AskProfile(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)

    def decode(self):
        self.HighID = self.read_int()
        self.LowID = self.read_int()

    def process(self):
        db = DataBase(self.player)
        self.players = db.getAllPlayers()
        Profile(self.device, self.player, self.HighID, self.LowID, self.players).Send()
