import math
import time
from Packets.Messages.Server.VisionUpdateMessage import VisionUpdateMessage
from Utils.BitStream import BitStream
from Database.DatabaseManager import DataBase
class LogicMovement(BitStream):
    def __init__(self, device):
        self.device = device
        
    
    def move_to(self, player, target_x, target_y, target_z=0, speed=500, duration=2.0, interval=0.05):
        """This is a completly shitty way to make charges i absolutely need to code it better, if only i could find the function on lib.."""
        db = DataBase(player)
        battleInfo = db.getBattleInfo([player.battleID])[0]
        objectInfos = battleInfo["gameObjects"]["gameObjects"]["heroes"]["1"]["objectInfos"]

        start_x, start_y = objectInfos["x"], objectInfos["y"]
        total_distance = math.dist([start_x, start_y], [target_x, target_y])
        travel_time = min(total_distance / speed, duration) 
        start_time = time.time()

        while time.time() - start_time < travel_time:
            elapsed_time = time.time() - start_time
            t = min(elapsed_time / travel_time, 1)
            objectInfos["x"] = int((1 - t) * start_x + t * target_x)
            objectInfos["y"] = int((1 - t) * start_y + t * target_y)

            objectInfos["z"] = int(target_z * (1 - (2 * (t - 0.5)) ** 2))

            # Update battle state
            db.updateBattle(self.player.battleID, battleInfo)
            VisionUpdateMessage(self.device, player).Send()

            time.sleep(interval)  # Smooth updates

        # Ensure final position is exactly at target
        objectInfos["x"], objectInfos["y"], objectInfos["z"] = target_x, target_y, 0
        db.updateBattle(self.player.battleID, battleInfo)
        VisionUpdateMessage(self.device, player).Send()