from Utils.Writer import Writer
import time


class MatchMakingStatusMessage(Writer):
    def __init__(self, device, player, matchmakeState, seconds):
        self.device = device
        self.id = 20405
        self.player = player
        self.seconds = seconds
        self.matchmakeState = matchmakeState
        super().__init__(self.device)


    def encode(self):
        self.writeInt(self.seconds) # Matchmake Timer
        self.writeInt(1) # Current Players in Matchmake
        
        self.writeString(self.player.name)
        self.writeBoolean(self.matchmakeState)
        self.writeInt(self.player.HighID)
        self.writeInt(self.player.LowID)
        self.writeInt(2) # Maximum Players in Matchmake
