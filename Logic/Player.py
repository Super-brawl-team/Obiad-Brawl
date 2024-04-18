class Player:

    HighID = 0
    LowID = 1
    Token = None
    name = "PrimoDEVHacc"
    eventCount = 4
    teamID = 0
    teamStatus = 0
    isReadyState = False
    selectedCard = (16, 0)
    isTeamInPracticeMode = False
    teamEventIndex = 0
    teamType = 0
    teamStreamMessageCount = 0
    isAdvertiseToBand = False

    def __init__(self, device):
        self.device = device

    def encode(self):
        return None
