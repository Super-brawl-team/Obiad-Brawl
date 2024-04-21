from Packets.Messages.Server.VisionUpdateMessage import VisionUpdateMessage
from Packets.Messages.Server.StartLoadingMessage import StartLoadingMessage
from Packets.Messages.Server.UDPConnectionInfoMessage import UDPConnectionInfoMessage

import time
from threading import Thread

class LogicBattle(Thread):
    def __init__(self, device, player):
        Thread.__init__(self)
        self.device = device
        self.player = player
        self.tick = 0
        self.started = 0
    
    def run(self):
        self.startBattle()
    
    def startBattle(self):
        self.started = 1
        StartLoadingMessage(self.device, self.player).Send()
        UDPConnectionInfoMessage(self.device, self.player).Send()
        while self.started:
            self.tick += 1
            self.player.battleTicks = self.tick
            self.process()
            time.sleep(0.045)

    def process(self):
        VisionUpdateMessage(self.device, self.player).Send()