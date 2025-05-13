from Packets.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Utils.Reader import ByteStream
from Database.DatabaseManager import DataBase

class GoHomeFromOfflineMessage(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        pass

    def process(self):
        db = DataBase(self.player)
        if self.player.tutorialState < 2:
            self.player.tutorialState += 1
            db.replaceValue("tutorialState", self.player.tutorialState)
        OwnHomeDataMessage(self.device, self.player).Send() # 14109