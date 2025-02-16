# -*- coding: utf-8 -*-
from Utils.Writer import Writer


class AllianceEventMessage(Writer):

    def __init__(self, device, player, event):
        self.id = 24333
        self.device = device
        self.event = event
        self.player = player
        super().__init__(self.device)

    def encode(self):
        self.writeVInt(self.event)
