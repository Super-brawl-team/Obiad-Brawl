# -*- coding: utf-8 -*-

from Packets.Messages.Server.KeepAliveOk import KeepAliveOk
from Utils.Reader import ByteStream


class KeepAlive(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass

    def process(self):
        KeepAliveOk(self.device).Send()
