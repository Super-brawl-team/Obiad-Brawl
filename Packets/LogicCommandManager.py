from Packets.Commands.Client.LogicGatchaCommand import LogicGatchaCommand
from Packets.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand
from Packets.Commands.Client.LogicBuyCard import LogicBuyCardCommand
from Packets.Commands.Client.LogicSelectBattleHints import LogicSelectBattleHintsCommand
from Packets.Commands.Client.LogicSelectControlMode import LogicSelectControlModeCommand

commands = {
    203: LogicGiveDeliveryItemsCommand,
    500: LogicGatchaCommand,
    502: LogicBuyCardCommand,
    509: LogicSelectControlModeCommand,
    513: LogicSelectBattleHintsCommand
}