from Utils.Writer import Writer
from Entries.LogicConfData import LogicConfData
from Entries.LogicDailyData import LogicDailyData

class LogicDayChangedCommand(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.id = 24111
        self.player = player
        self.device = device


    def encode(self, booleans):
        "For unknown reasons this command crashes, please do not use it"
        self.writeBoolean(booleans["RefreshLogicDailyData"])
        if booleans["RefreshLogicDailyData"]:
            LogicDailyData.encode(self, self.player)
        self.writeBoolean(booleans["RefreshLogicConfData"])
        if booleans["RefreshLogicConfData"]:
            LogicConfData.encode(self, self.player)