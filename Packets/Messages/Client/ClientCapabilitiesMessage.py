from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Player

from Utils.Reader import ByteStream


class ClientCapabilitiesMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.ping = self.readVInt()
        print(f"[*] User's latency : {self.ping} ")

    def process(self):
        pass