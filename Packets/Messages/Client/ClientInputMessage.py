from Utils.Reader import ByteStream
from Packets.Messages.Server.VisionUpdateMessage import VisionUpdateMessage
from Logic.Battle.Tick.LogicMovement import LogicMovement
from Logic.Player import Player
from Database.DatabaseManager import DataBase
from Files.CsvLogic.Skills import Skills
class ClientInputMessage(ByteStream):
    def __init__(self, data, device, player):
        super().__init__(data)
        self.device = device
        self.data = data
        self.player = player

    def decode(self):
        db = DataBase(self.player)
        battleInfo = db.getBattleInfo([self.player.battleID])[0]
        self.readVInt()
        self.readVInt()
        self.count = self.readVInt()
        for x in range(self.count):
          unk = self.readVInt() # idk index?
          self.readVInt() # index?
          type = self.readVInt() # (0 : Attack, 100 : Move)
          x = self.readVInt()
          y = self.readVInt()
          if type == 100:
            battleInfo["gameObjects"]["gameObjects"]["heroes"]["1"]["objectInfos"]["x"] = x
            battleInfo["gameObjects"]["gameObjects"]["heroes"]["1"]["objectInfos"]["y"] = y

            db.updateBattle(self.player.battleID, battleInfo)
          elif type == 107:
            battleInfo["gameObjects"]["gameObjects"]["heroes"]["1"]["ultiAiming"] = True
            db.updateBattle(self.player.battleID, battleInfo)
          elif type == 108:
            battleInfo["gameObjects"]["gameObjects"]["heroes"]["1"]["ultiAiming"] = False
            db.updateBattle(self.player.battleID, battleInfo)

          else:
            if type < 100 and type >= 0:
            # handle skills
              if Skills.getSpecifiedSkillInfo(self, type, "BehaviorType") == "Charge":
                chargeType = int(Skills.getSpecifiedSkillInfo(self, type, "ChargeType"))
                if chargeType == 2:
                  LogicMovement(self.device).move_to(self.player, x, y, int(Skills.getSpecifiedSkillInfo(self, type, "ChargeSpeed"))*2, speed=int(Skills.getSpecifiedSkillInfo(self, type, "ChargeSpeed")))
                elif chargeType == 4:
                  LogicMovement(self.device).move_to(self.player, x, y, speed=int(Skills.getSpecifiedSkillInfo(self, type, "ChargeSpeed")))
              #print(f"unhandled skill: {type}")
          

    def process(self):
        #self.player.battleTicks += 1
        VisionUpdateMessage(self.device, self.player).Send()
