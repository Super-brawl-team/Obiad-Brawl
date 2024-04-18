# -*- coding: utf-8 -*-


class Player:

    HighID = 0
    LowID = 0
    Token = None
    name = "PrimoDEVHacc"
    eventCount = 4
    teamID = 0
    teamStatus = 0
    isReadyState = False

    def __init__(self, device):
        self.device = device

    def encode(self):
        return None
