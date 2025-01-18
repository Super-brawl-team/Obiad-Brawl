from Packets.Messages.Server.TeamMessage import TeamMessage
from Utils.Reader import ByteStream
from Logic.Player import Player


class TeamTogglePractiseMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        pass
        

    def process(self):
        if self.player.isTeamInPracticeMode == True:
           self.player.isTeamInPracticeMode = False
        else:
            self.player.isTeamInPracticeMode = True 
        TeamMessage(self.device, self.player).Send()