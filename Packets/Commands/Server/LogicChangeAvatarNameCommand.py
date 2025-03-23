from Utils.Writer import Writer


class LogicChangeAvatarNameCommand(Writer):

    def __init__(self, device, player, state):
        super().__init__(device)
        self.id = 24111
        self.player = player
        self.state = state
        self.device = device


    def encode(self):
        self.writeVInt(201)
        self.writeString(self.player.name)
        self.writeVInt(self.state) # state
        