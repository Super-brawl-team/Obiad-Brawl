from Utils.Reader import ByteStream
from random import choice
from string import ascii_uppercase
import json
from Logic.Player import Player
from Packets.Messages.Server.Leaderboards import Leaderboard

class GetLeaderboardMessage(ByteStream):
    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)

    def decode(self):
        self.device.LeaderboardType = self.ReadVint()
        self.device.LeaderboardInfo = self.ReadVint()


    def process(self):
    
       Leaderboard(self.device).Send()

