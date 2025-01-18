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
        
<<<<<<< Updated upstream
        self.writeVInt(23)
        self.writeVInt(0)
=======
<<<<<<< HEAD
        self.writeDataReference(15, 0) # map pour
=======
        self.writeVInt(23)
        self.writeVInt(0)
>>>>>>> 54c5ae3525afb6f57f42905c8081514084a01e2b
>>>>>>> Stashed changes
