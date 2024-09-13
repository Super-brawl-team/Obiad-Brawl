from Packets.Messages.Server.TeamStreamMessage import TeamStreamMessage
import random
from Logic.Player import Player
from Utils.Reader import ByteStream


class TeamChatMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        self.messageContent = self.readString()


    def process(self):
        TeamStreamMessage(self.device, self.player, self.messageContent).Send()