# -*- coding: utf-8 -*-

from Packets.Messages.Server.Profile import Profile
from Utils.Reader import ByteStream
from Logic.Player import Player


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
        self.players = 0
        Profile(self.device, self.player, self.HighID, self.LowID, self.players).Send()
