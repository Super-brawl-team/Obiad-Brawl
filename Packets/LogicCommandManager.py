from Packets.Commands.Client.LogicGatchaCommand import LogicGatchaCommand
<<<<<<< Updated upstream

commands = {
    500: LogicGatchaCommand
=======
from Packets.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand
from Packets.Commands.Client.LogicBuyCard import LogicBuyCardCommand


commands = {
    203: LogicGiveDeliveryItemsCommand,
    500: LogicGatchaCommand,
    502: LogicBuyCardCommand
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
}