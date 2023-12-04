# -*- coding: utf-8 -*-
from Packets.Messages.Client import *


availablePackets = {

    10101: Login,
    10108: KeepAlive,
    10212: ChangeAvatarNameMessage,
    14102: Commands,
    14109: GoHomeFromOffline,
    14110: AskForBattleEnd,
    14113: AskProfile,
    14301: AskForClan,
    14302: AskForClan,
    14403: GetLeaderboardMessage
}
