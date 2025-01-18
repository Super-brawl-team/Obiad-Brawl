from Logic.Player import Player
from Packets.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Database.DatabaseManager import DataBase
from Utils.Reader import ByteStream

class LogicSelectControlModeCommand(ByteStream):
    def __init__(self, device, player, data):
        super().__init__(data)
        self.player = player
        self.device = device

    def decode(self):
        self.readCommandHeader()
        self.control_mode = self.readVInt()
        
    def encode(self, mode):
        for x in range(8):
            self.writeVInt()
        self.writeVInt(509)
        self.writeVInt(mode)

    def process(self):
        db = DataBase(self.player)
        if self.control_mode < 0:
            return "no cheating lol"
            
        elif self.control_mode > 2:
            return "no cheating lol"
        self.player.control_mode = self.control_mode
        db.replaceValue("control_mode", self.player.control_mode)
        
        