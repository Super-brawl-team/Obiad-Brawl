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
        
        self.writeString("erzkw78p83t73sbm6c4ms2ww8894fynmzc3xyntf");
        self.writeString("467606826913688")
        self.writeString("G:325378671")
        
        self.writeInt(2)
        self.writeInt(57)
        self.writeInt(2)
        
        self.writeString("integration")
        
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeString()
        self.writeString()
        self.writeString()
        
        self.writeInt(0)
        
        self.writeString()
        self.writeString("EN")
        self.writeString()
        
        self.writeInt(1)
        
        self.writeString()
        self.writeString()
        self.writeString()
