class LogicCharacterServer:
    def setDefaultStartRotation(playerTeam):
        defaultStartRotation = 270
        if playerTeam == 1:
            defaultStartRotation = 90
        return defaultStartRotation