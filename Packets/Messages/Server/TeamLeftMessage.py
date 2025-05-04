from Utils.Writer import Writer


class TeamLeftMessage(Writer):

    def __init__(self, device, player, reason):
        self.id = 24125
        self.device = device
        self.player = player
        self.reason = reason
        super().__init__(self.device)

    def encode(self):
        self.writeInt(self.reason) #I suppose leave reason