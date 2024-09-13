from Utils.Reader import ByteStream
from Logic.Player import Player


class ClientHelloMessage(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        print(self.readInt())
        print(self.readInt())
        print(self.readInt())
        print(self.readInt())
        print(self.readInt())
        print(self.readString())
        print(self.readInt())
        print(self.readInt())


    def process(self):
        pass
