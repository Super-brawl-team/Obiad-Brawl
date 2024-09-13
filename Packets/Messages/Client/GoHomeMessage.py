from Packets.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Utils.Reader import ByteStream


class GoHomeMessage(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        pass

    def process(self):
        OwnHomeDataMessage(self.device, self.player).Send() # 14109