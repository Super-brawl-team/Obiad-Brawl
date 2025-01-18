from Packets.Messages.Server.TeamMessage import TeamMessage
from Utils.Reader import ByteStream
from Logic.Player import Player


class TeamChangeMemberSettingsMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player


    def decode(self):
        self.readVInt()
        self.player.selectedCard = self.readDataReference()


    def process(self):
        TeamMessage(self.device, self.player).Send()