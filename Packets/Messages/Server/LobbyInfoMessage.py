from Utils.Writer import Writer


class LobbyInfoMessage(Writer):

    def __init__(self, device, player, players):
        self.id = 23457
        self.device = device
        self.player = player
        self.players = players
        super().__init__(self.device)

    def encode(self):
        self.writeVint(self.players) # Players Online
        
        
        # Lobby Info Entry Array
        self.writeVint(0) # Count
        for x in range(0):
            self.writeVint(1)
            self.writeVint(1)
            self.writeVint(1)
            self.writeVint(1)
            self.writeVint(1)