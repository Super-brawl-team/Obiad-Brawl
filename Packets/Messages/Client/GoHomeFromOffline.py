# -*- coding: utf-8 -*-

from Packets.Messages.Server.OwnHomeData import OwnHomeData
from Utils.Reader import ByteStream


class GoHomeFromOffline(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass

    def process(self):
        OwnHomeData(self.device).Send() # 14109