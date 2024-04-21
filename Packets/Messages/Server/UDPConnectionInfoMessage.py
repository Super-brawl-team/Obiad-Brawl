from Utils.Writer import Writer

class UDPConnectionInfoMessage(Writer):

    def __init__(self, device, player):
        self.id = 24112
        self.device = device
        self.player = player
        super().__init__(self.device)


    def encode(self):
        self.writeVInt(9449) # Server Port
        self.writeString("127.0.0.1") # Server IP
        self.writeBytes() # unk
        #self.writFilteredString() # unk


