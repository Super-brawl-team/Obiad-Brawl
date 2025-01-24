from Utils.Reader import ByteStream
from Packets.Messages.Server.VisionUpdateMessage import VisionUpdateMessage
from Logic.Player import Player

class ClientInputMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.count = self.readVInt()
        for x in range(self.count):
          unk = self.readVInt() # idk index?
          self.readVInt() # index?
          type = self.readVInt() # (0 : Attack, 100 : Move)
          x = self.readVInt()
          y = self.readVInt()
          if type == 100:
            self.player.x = x
            self.player.y = y
            print(f"Player moved to {self.player.x}, {self.player.y}")
          elif type == 0:
            print(f"Player attacked and given coordinates are {x}, {y}")
          else: 
            print("unhandled type")

    def process(self):
        #self.player.battleTicks += 1
        pass
        #VisionUpdateMessage(self.device, self.player).Send()
