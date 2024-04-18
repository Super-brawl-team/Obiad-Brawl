from Utils.Writer import Writer


class MatchMakingStatusMessage(Writer):
    def __init__(self, device, player, matchmakeState):
        self.device = device
        self.id = 20405
        self.player = player
        self.matchmakeState = matchmakeState
        super().__init__(self.device)


    def encode(self):
        self.writeInt(20) # Matchmake Timer
        self.writeInt(1) # Current Players in Matchmake
        
        self.writeString(self.player.name)
        self.writeBoolean(self.matchmakeState)
        self.writeInt(self.player.high_id)
        self.writeInt(self.player.low_id)
        self.writeInt(2) # Maximum Players in Matchmake