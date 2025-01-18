from Utils.Writer import Writer


class LogicChangeAvatarNameCommand(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.id = 24111
        self.player = player
        self.device = device


    def encode(self):
        self.writeVInt(201)
        self.writeString(self.player.name)
        self.writeByte(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        