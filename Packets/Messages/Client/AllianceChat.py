from Utils.Reader import ByteStream
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Packets.Messages.Server.AllianceChatServer import AllianceChatServer

class AllianceChat(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player
        self.HighID = 0
        self.LowID = 0

    def decode(self):
        self.msg = self.readString()
    
    def process(self):
        db = DataBase(self.player)
        """You can add your chat commands here if u want, here is a simple example to add 9999 gems to your account:
        if self.msg.lower() == "/addgems":
           AvailableServerCommandMessage(self.device, self.player, 202, 9999).Send()
           return
       """
        db.addMsg(self.player.club_id, 2, self.player.low_id, self.player.name, self.player.club_role, self.msg, 0)
        db.loadClub(self.player.club_id)
        self.plrids = []
        club =  db.loadClub(self.player.club_id)
        nextKey = db.getNextKey(self.player.club_id)
        for token in club["info"]["memberCount"]:
            memberData = db.getMemberData(token)
            self.plrids.append(memberData["low_id"])
        for low_id in self.plrids:
            AllianceChatServer(self.device, self.player, self.player.club_id, nextKey+1).SendTo(low_id)