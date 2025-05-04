# -*- coding: utf-8 -*-

from Packets.Messages.Server.KeepAliveOkMessage import KeepAliveOkMessage
from Utils.Reader import ByteStream
from Packets.Messages.Server.MyAlliance import MyAlliance

class KeepAliveMessage(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        pass

    def process(self):
        KeepAliveOkMessage(self.device, self.player).Send()
        try: 
            MyAlliance(self.device, self.player).Send()
        except:
            pass
