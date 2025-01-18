# -*- coding: utf-8 -*-

from Utils.Reader import ByteStream
from Packets.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand
from Logic.Player import Player


class ChangeAvatarNameMessage(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.player.name = self.readString()

    def process(self):
        LogicChangeAvatarNameCommand(self.device, self.player).Send()
