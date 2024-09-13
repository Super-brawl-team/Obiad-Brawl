from Packets.Commands.Client.LogicGatchaCommand import LogicGatchaCommand
from Packets.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand


commands = {
    203: LogicGiveDeliveryItemsCommand,
    500: LogicGatchaCommand
}