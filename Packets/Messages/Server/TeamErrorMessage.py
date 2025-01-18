from Utils.Writer import Writer


class TeamErrorMessage(Writer):

    def __init__(self, device, player, error):
        self.id = 24129
        self.device = device
        self.player = player
        self.error = error
        super().__init__(self.device)

    def encode(self):
<<<<<<< Updated upstream
        self.writeInt(self.error) # Error TID
=======
<<<<<<< HEAD
        self.writeVInt(self.error) # Error TID
        self.writeVInt(0)
=======
        self.writeInt(self.error) # Error TID
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
