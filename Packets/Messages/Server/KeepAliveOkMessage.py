# -*- coding: utf-8 -*-
from Utils.Writer import Writer


class KeepAliveOkMessage(Writer):

    def __init__(self, device, player):
        self.id = 20108
        self.device = device
        self.player = player
        super().__init__(self.device)

    def encode(self):
        pass
