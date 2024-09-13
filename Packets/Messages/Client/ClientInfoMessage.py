from Logic.Player import Player
from Utils.Reader import ByteStream


class ClientInfoMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.info = self.readString()


    def process(self):
        print("[*] client battle info: " , self.info)