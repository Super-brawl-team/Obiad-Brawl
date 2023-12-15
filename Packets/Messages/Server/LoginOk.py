# -*- coding: utf-8 -*-

import time
from Utils.Writer import Writer


class LoginOk(Writer):

    def __init__(self, device):
        self.id = 20104
        self.version = 1
        self.device = device
        super().__init__(self.device)

    def encode(self):
        self.writeInt(0)
        self.writeInt(1)
        
        self.writeInt(0)
        self.writeInt(1)
        
        self.writeString("ObiadJestGotowy");
        self.writeString("467606826913688")
        self.writeString("G:325378671")
        
        self.writeInt(2)
        self.writeInt(57)
        self.writeInt(2)
        
        self.writeString("dev")
        
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeString()
        self.writeString()
        self.writeString()
        
        self.writeInt(0)
        
        self.writeString()
        self.writeString("FR")
        self.writeString()
        
        self.writeInt(1)
        
        self.writeString()
        self.writeString()
        self.writeString()
