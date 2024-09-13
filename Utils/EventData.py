from Files.CsvLogic.Locations import Locations

class EventData:
    def getGameModeVariation(self, location):
     variationString = Locations().GetGameModeString(self, location)
     if variationString == "CoinRush":
        gameModeVariation = 0
     elif variationString == "AttackDefend":
        gameModeVariation = 2
     elif variationString == "BossFight":
        gameModeVariation = 7
     elif variationString == "BountyHunter":
        gameModeVariation = 3
     elif variationString == "Artifact":
        gameModeVariation = 4
     elif variationString == "LaserBall":
        gameModeVariation = 5
     elif variationString == "BattleRoyale":
        gameModeVariation = 6
     elif variationString == "BattleRoyaleTeam":
        gameModeVariation = 9
     elif variationString == "Survival":
        gameModeVariation = 8
     else:
        print("[ERROR] Wrong game mode!")
        gameModeVariation = -1
     return gameModeVariation