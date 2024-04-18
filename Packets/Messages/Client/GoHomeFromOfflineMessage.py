from Packets.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Utils.Reader import ByteStream


class GoHomeFromOfflineMessage(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass

    def process(self):
        OwnHomeDataMessage(self.device).Send() # 14109