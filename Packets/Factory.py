# -*- coding: utf-8 -*-
from Packets.Messages.Client import *


availablePackets = {

    10101: LoginMessage,
    10107: ClientCapabilitiesMessage,
    10108: KeepAliveMessage,
    10212: ChangeAvatarNameMessage,
    14102: EndClientTurnMessage,
    14103: MatchmakeRequestMessage,
    14109: GoHomeFromOffline,
    14110: AskForBattleEnd,
    14113: AskProfile,
    14301: AskForClan,
    14302: AskForClan,
    14350: TeamCreateMessage,
    14351: TeamJoinMessage,
    14352: TeamKickMessage,
    14353: TeamLeaveMessage,
    14354: TeamChangeMemberSettingsMessage,
    14355: TeamSetMemberReadyMessage,
    14356: TeamTogglePractiseMessage,
    14357: TeamToggleMemberSideMessage,
    14358: TeamSpectateMessage,
    14359: TeamChatMessage,
    14360: TeamPostAdMessage,
    14361: TeamMemberStatusMessage,
    14403: GetLeaderboardMessage
}
