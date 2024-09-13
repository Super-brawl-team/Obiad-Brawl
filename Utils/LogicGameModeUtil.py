from Logic.Battle.LogicBattleModeServer import LogicBattleModeServer
class LogicGameModeUtil:
  def getBattleTicks(gameModeVariation):

    if LogicBattleModeServer.ART_TEST:
      return 99999999
    else:
      if gameModeVariation== 9 or gameModeVariation == 6:
        return LogicBattleModeServer.BATTLE_ROYALE_TICKS  # 16000 (800s or 6s of intro + 13m14s of battle)
      elif gameModeVariation == 5:
        return LogicBattleModeServer.LASER_BALL_TICKS  # 4280 (214s or 4s of intro + 3m of battle + 30s of overtime)
      elif gameModeVariation == 7:
        return LogicBattleModeServer.BOSS_FIGHT_TICKS  # 9680 (484s or 4s of intro + 8m of battle)
      else:
        return LogicBattleModeServer.NORMAL_TICKS  # 3080 (150s or 4s of intro + 2m30s of battle)