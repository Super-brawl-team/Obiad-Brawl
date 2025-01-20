from Utils.Writer import Writer

class UDPConnectionInfoMessage(Writer):

    def __init__(self, device, player):
        self.id = 24112
        self.device = device
        self.player = player
        super().__init__(self.device)


    def encode(self):
        self.writeVInt(9449) # Server Port
        self.writeString("192.168.1.184") # Server IP
        self.writeBytes(b"0123456789") # session token
        self.writeStringReference("nonce") # the string explains it


