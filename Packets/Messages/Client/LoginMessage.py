from Utils.Reader import ByteStream
from Packets.Messages.Server.LoginOkMessage import LoginOkMessage
from Packets.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Packets.Messages.Server.ClanData import ClanData
from Packets.Messages.Server.ClanStream import ClanStream
from Logic.Player import Player


class LoginMessage(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)

    def decode(self):
        pass

    def process(self):
        LoginOkMessage(self.device).Send()
        ClanStream(self.device, self.device.Player).Send() # 14109
        OwnHomeDataMessage(self.device).Send()
        ClanData(self.device, self.device.Player).Send() # 14109
