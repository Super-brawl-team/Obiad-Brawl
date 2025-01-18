# -*- coding: utf-8 -*-


class Player:

<<<<<<< Updated upstream
    HighID = 0
    LowID = 0
    Token = None
    name = "PrimoDEVHacc"
=======
    high_id = 0
    low_id = 1
    token = None
    usedVersion = 1
    name = "Brawler"
    eventCount = 4
    highest_trophies = 0
    teamID = 0
    teamStatus = 0
    isReady = False
    selectedCard = [16, 0]
    isTeamInPracticeMode = False
    teamEventIndex = 0
    teamType = 0
    teamStreamMessageCount = 0
    isAdvertiseToBand = False
    matchmakeStartTime = 0
    battleTicks = 0
    wifi = 0
    region = "CAT"
    player_status = 3
    last_connection_time = 0
    friends = {}
    room_id = 0
    unlocked_brawlers = {
        0: {'Cards': {0: 1}, 'Skins': [0], 'selectedSkin': 0, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 0, 'PowerPoints': 0, 'State': 2, 'StarPower': 0}}
    player_experience = 0
    profile_icon = 0
    trophies = 0
    solo_wins = 0
    duo_wins = 0
    ThreeVSThree_wins = 0
    gems = 0
    gold = 92
    chips = 0
    elexir = 0
    coinsdoubler = 0
    coinsbooster = 0
    coins_reward = 0
    map_id = 7
    skin_id = 0
    brawler_id = 0
    team = 0
>>>>>>> Stashed changes

    def __init__(self, device):
        self.device = device

    def encode(self):
        return None
