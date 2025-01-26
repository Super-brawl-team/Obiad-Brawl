from Packets.Commands.Client.LogicGatchaCommand import LogicGatchaCommand
from Packets.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand
from Packets.Commands.Client.LogicBuyCard import LogicBuyCardCommand
from Packets.Commands.Client.LogicSelectBattleHints import LogicSelectBattleHintsCommand
from Packets.Commands.Client.LogicSelectControlMode import LogicSelectControlModeCommand
from Packets.Commands.Client.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from Packets.Commands.Client.LogicBuyCoinsBoosterCommand import LogicBuyCoinsBoosterCommand
from Packets.Commands.Client.LogicBuyCoinsDoublerCommand import LogicBuyCoinsDoublerCommand
commands = {
    203: LogicGiveDeliveryItemsCommand,
    500: LogicGatchaCommand,
    502: LogicBuyCardCommand,
    506: LogicSetPlayerThumbnailCommand,
    509: LogicSelectControlModeCommand,
    510: LogicBuyCoinsDoublerCommand,
    511: LogicBuyCoinsBoosterCommand,
    513: LogicSelectBattleHintsCommand
}