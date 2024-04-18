# -*- coding: utf-8 -*-

from Packets.Messages.Server.KeepAliveOkMessage import KeepAliveOkMessage
from Utils.Reader import ByteStream


class KeepAliveMessage(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass

    def process(self):
        KeepAliveOkMessage(self.device).Send()
