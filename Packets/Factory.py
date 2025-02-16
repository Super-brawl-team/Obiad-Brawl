# -*- coding: utf-8 -*-
from Packets.Messages.Client import *


availablePackets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10107: ClientCapabilitiesMessage,
    10108: KeepAliveMessage,
    10177: ClientInfoMessage,
    10212: ChangeAvatarNameMessage,
    10555: ClientInputMessage,
    14101: GoHomeMessage,
    14102: EndClientTurnMessage,
    14103: MatchmakeRequestMessage,
    14109: GoHomeFromOfflineMessage,
    14110: AskForBattleEndMessage,
    14113: AskProfile,
    14301: AllianceCreate,
    14302: AskForClan,
    14305: AllianceJoin,
    14308: AllianceLeave,
    14315: AllianceChat,
    14316: AllianceEditSettings,
    14350: TeamCreateMessage,
    14351: TeamJoinMessage,
    #14352: TeamKickMessage, i forgor
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
