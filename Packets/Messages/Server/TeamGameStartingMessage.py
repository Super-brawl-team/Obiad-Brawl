from Utils.Writer import Writer


class TeamGameStartingMessage(Writer):

    def __init__(self, device, player):
        self.id = 24130
        self.player = player
        self.device = device
        super().__init__(self.device)

    def encode(self):
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeDataReference(15, 0) # map pour