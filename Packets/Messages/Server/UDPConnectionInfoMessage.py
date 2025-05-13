from Utils.Writer import Writer
import json

class UDPConnectionInfoMessage(Writer):

    def __init__(self, device, player):
        self.id = 24112
        self.device = device
        self.player = player
        super().__init__(self.device)


    def encode(self):
        self.writeVInt(json.load(open("Settings.json"))["UDPPort"]) # Server Port
        self.writeString(json.load(open("Settings.json"))["UDPAddress"]) # Server IP
        self.writeBytes(b"0123456789") # session token
        self.writeStringReference("nonce") # the string explains it


