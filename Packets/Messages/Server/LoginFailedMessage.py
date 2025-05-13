from Utils.Writer import Writer
import json

class LoginFailedMessage(Writer):

    def __init__(self, device, player, loginPayload, msg , errorCode):
        super().__init__(device)
        self.id = 20103
        self.device = device
        self.player = player
        self.loginPayload = loginPayload
        self.msg = msg
        self.errorCode = errorCode


    def encode(self):
        self.writeInt(self.errorCode)
        self.writeString(self.loginPayload["fingerprintData"])
        self.writeString() # Server Host
        settings = json.load(open("Settings.json"))
        self.writeString(f"http://{settings['gameAssetsAddress']}:{settings['gameAssetsPort']}]/")
        self.writeString("https://github.com/Super-brawl-team/Obiad-Brawl")
        self.writeString(self.msg)

        self.writeInt(0) # maintenance time
        self.writeBoolean(False) # Show support page

        self.writeString()
        self.writeString()

        self.writeInt(0)
        self.writeInt(3)

        self.writeString()
        self.writeString()

        self.writeInt(0)
        self.writeInt(0)

        self.writeBoolean(False)
        self.writeBoolean(False)



