# -*- coding: utf-8 -*-

from Utils.Reader import ByteStream
from Packets.Messages.Server.LoginOk import LoginOk
from Packets.Messages.Server.OwnHomeData import OwnHomeData
from Packets.Messages.Server.ClanData import ClanData
from Packets.Messages.Server.ClanStream import ClanStream
from Logic.Player import Player


class Login(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)

    def decode(self):
        pass

    def process(self):
        LoginOk(self.device).Send()
        ClanStream(self.device, self.device.Player).Send() # 14109
        OwnHomeData(self.device).Send()
        ClanData(self.device, self.device.Player).Send() # 14109
