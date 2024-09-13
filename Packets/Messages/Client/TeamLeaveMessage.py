from Packets.Messages.Server.TeamLeftMessage import TeamLeftMessage
from Utils.Reader import ByteStream
from Logic.Player import Player


class TeamLeaveMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        pass
        

    def process(self):
        self.player.teamID = 0
        self.player.teamStreamMessageCount = 0
        TeamLeftMessage(self.device, self.player).Send()