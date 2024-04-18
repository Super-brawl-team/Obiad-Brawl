# -*- coding: utf-8 -*-
from Packets.Messages.Client import *


availablePackets = {

    10101: Login,
    10107: ClientCapabilitiesMessage,
    10108: KeepAlive,
    10212: ChangeAvatarNameMessage,
    14102: Commands,
    14109: GoHomeFromOffline,
    14110: AskForBattleEnd,
    14113: AskProfile,
    14301: AskForClan,
    14302: AskForClan,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14363: TeamSetLocationMessage,
    14354: TeamChangeMemberSettingsMessage,
    14361: TeamMemberStatusMessage,
    14362: TeamSetRankedLocationMessage,
    14363: TeamSetLocationMessage,
    14403: GetLeaderboardMessage
}
