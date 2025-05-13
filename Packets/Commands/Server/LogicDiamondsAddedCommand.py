from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class LogicDiamondsAddedCommand(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.id = 24111
        self.player = player
        self.device = device


    def encode(self, diamonds):
        db = DataBase(self.player)
        self.writeByte(0)
        self.writeInt(diamonds)
        self.writeInt(0)
        self.writeInt(0)
        self.writeString("hhh")
        self.writeVInt(0)
        self.player.gems += diamonds
        db.replaceValue("gems", self.player.gems)