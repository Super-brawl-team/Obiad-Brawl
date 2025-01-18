from Utils.Writer import Writer


class TeamLeftMessage(Writer):

    def __init__(self, device, player):
        self.id = 24125
        self.device = device
        self.player = player
        super().__init__(self.device)

    def encode(self):
        self.writeInt(0) # Error TID