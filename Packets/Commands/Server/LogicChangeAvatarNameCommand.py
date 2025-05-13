from Utils.Writer import Writer


class LogicChangeAvatarNameCommand(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.id = 24111
        self.player = player
        self.device = device


    def encode(self, state):
        self.writeString(self.player.name)
        self.writeVInt(state) # state
        