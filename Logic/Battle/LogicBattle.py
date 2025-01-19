from Packets.Messages.Server.VisionUpdateMessage import VisionUpdateMessage
from Packets.Messages.Server.StartLoadingMessage import StartLoadingMessage
from Packets.Messages.Client.ForceSendBattleEnd import ForceSendBattleEnd
from Packets.Messages.Server.UDPConnectionInfoMessage import UDPConnectionInfoMessage

import time
from threading import Thread

class LogicBattle(Thread):
    def __init__(self, device, player):
        Thread.__init__(self)
        self.device = device
        self.player = player
        self.player.battleTicks = 0
        self.subTick = 0
        self.started = 0
    
    def run(self):
        self.startBattle()
    
    def startBattle(self):
        self.started = 1
        StartLoadingMessage(self.device, self.player).Send()
        while self.started:
           if self.player.battleTicks > 1000:
              self.started = 0
              ForceBattleEnd = ForceSendBattleEnd(self.device, self.player)
              ForceBattleEnd.decode()
              ForceBattleEnd.process()
           else:
            if self.subTick >= 4:
                self.player.battleTicks += 1
                self.subTick = 0
                #print("Tick: ", self.tick)
            self.process()
            time.sleep(0.003)

    
    def process(self):
        VisionUpdateMessage(self.device, self.player).Send()
        self.subTick += 1