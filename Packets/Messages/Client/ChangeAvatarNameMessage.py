# -*- coding: utf-8 -*-

from Utils.Reader import ByteStream
from Packets.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Logic.Player import Player
from Database.DatabaseManager import DataBase

class ChangeAvatarNameMessage(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.player.name = self.readString()
        self.state = self.readVInt()
    def process(self):
        db = DataBase(self.player)
        db.replaceValue("name", self.player.name)
        AvailableServerCommandMessage(self.device, self.player, 201 ,self.state).Send()
