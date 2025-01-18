from Utils.Writer import Writer


class TeamErrorMessage(Writer):

    def __init__(self, device, player, error):
        self.id = 24129
        self.device = device
        self.player = player
        self.error = error
        super().__init__(self.device)

    def encode(self):
        self.writeVInt(self.error) # Error TID
        self.writeVInt(0)