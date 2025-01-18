from Utils.Reader import ByteStream
from random import choice
from string import ascii_uppercase
import json
from Logic.Player import Player
from Packets.Messages.Server.LeaderboardMessage import LeaderboardMessage

class GetLeaderboardMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.device.LeaderboardType = self.readVInt()
        self.device.LeaderboardInfo = self.readVInt()
        self.target = self.readDataReference()


    def process(self):
    
       LeaderboardMessage(self.device, self.player, self.target).Send()

