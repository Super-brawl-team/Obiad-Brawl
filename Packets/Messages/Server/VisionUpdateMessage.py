from Utils.Writer import Writer
import time


class VisionUpdate(Writer):
    def __init__(self, device, player):
        self.device = device
        self.id = 24109
        self.player = player
        super().__init__(self.device)


    def encode(self):
        self.writeInt(1)