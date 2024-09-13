# -*- coding: utf-8 -*-

import time
from Utils.Writer import Writer


class LoginOkMessage(Writer):

    def __init__(self, device, player, loginPayload):
        self.id = 20104
        self.version = 1
        self.player = player
        self.loginPayload = loginPayload
        self.device = device
        super().__init__(self.device)

    def encode(self):
        self.writeLong(self.loginPayload["highID"], self.loginPayload["lowID"]) # id
        
        self.writeLong(self.loginPayload["highID"], self.loginPayload["lowID"]) # id
        
        self.writeString(self.loginPayload["token"])
        self.writeString("467606826913688")
        self.writeString("G:325378671")
        
        self.writeInt(self.loginPayload["majorVersion"])
        self.writeInt(self.loginPayload["minorVersion"])
        self.writeInt(self.loginPayload["build"])
        
        self.writeString("-dev")
        
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeString()
        self.writeString()
        self.writeString()
        
        self.writeInt(0)
        
        self.writeString()
        self.writeString(self.loginPayload["region"])
        self.writeString()
        
        self.writeInt(1)
        
        self.writeString()
        self.writeString()
        self.writeString()
