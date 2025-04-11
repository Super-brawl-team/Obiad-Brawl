from Utils.Reader import ByteStream
from Packets.Messages.Server.LoginOkMessage import LoginOkMessage
from Packets.Messages.Server.LoginFailedMessage import LoginFailedMessage
from Packets.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Packets.Messages.Server.MyAlliance import MyAlliance
from Packets.Messages.Server.ClanStream import ClanStream
from Packets.Messages.Server.StartLoadingMessage import StartLoadingMessage
from Logic.Player import Player
from Logic.Battle.LogicBattle import LogicBattle
from Packets.Messages.Server.UDPConnectionInfoMessage import UDPConnectionInfoMessage
from Database.DatabaseManager import DataBase
from Utils.Helpers import Helpers
import time
import json
class LoginMessage(ByteStream):

    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.settings = json.load(open('Settings.json'))
        self.player = player

    def decode(self):
        self.loginPayload = {}
        self.loginPayload["highID"] = self.readInt()
        self.loginPayload["lowID"] = self.readInt()
        self.loginPayload["token"] = self.readString()
        self.loginPayload["majorVersion"] = self.readInt()
        self.loginPayload["minorVersion"] = self.readInt()
        self.loginPayload["build"] = self.readInt()
        self.loginPayload["fingerprintSHA"] = self.readString()
        self.loginPayload["unknownString1"] = self.readString()
        self.loginPayload["deviceID"] = self.readString()
        self.loginPayload["unknownString2"] = self.readString()
        self.loginPayload["device"] = self.readString()
        self.loginPayload["systemLanguage"] = self.readVInt()
        try:
            self.loginPayload["region"] = self.loginPayload["systemLanguage"] = self.readString().split('-')[1]
        except:
            self.loginPayload["region"] = self.loginPayload["systemLanguage"] = "EN"
        self.player.usedVersion = self.loginPayload["majorVersion"]

    def process(self):
        db = DataBase(self.player)
        print(self.loginPayload["token"])
        if self.player.usedVersion in (1, 2):
            if not db.is_token_in_table(self.loginPayload["token"]):
                if self.loginPayload["token"] is None:
                    self.loginPayload["token"] = self.player.token = Helpers.randomStringDigits(self)
                else:
                    self.player.token = self.loginPayload["token"]
                db.getPlayerId()
                db.createAccount()
                


            # Process login information
            self.player.high_d = self.loginPayload["highID"]
            self.player.low_id = self.loginPayload["lowID"]
            self.player.token = str(self.loginPayload["token"])
            self.player.region = self.loginPayload["region"]
            db.replaceValue("region", self.player.region)

            # Send success messages
            LoginOkMessage(self.device, self.player, self.loginPayload).Send()
            # 14109
            db.loadAccount()
            if self.player.battleID == 0:
                OwnHomeDataMessage(self.device, self.player).Send()
                ClanStream(self.device, self.player).Send()
                MyAlliance(self.device, self.player).Send()  # 14109
            else:
                
                StartLoadingMessage(self.device, self.player).Send()
                
                self.settings = json.load(open('Settings.json'))
                if self.settings["UseUDPServer"]:
                    UDPConnectionInfoMessage(self.device, self.player).Send() # its broken so please keep tcp
                else:
                    battle = LogicBattle(self.device, self.player)
                    battle.start()
        else:
            LoginFailedMessage(self.device, self.player, self.loginPayload, " ", 8).Send()
