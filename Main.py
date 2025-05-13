from threading import *
from Networking import *
from battle import *
import json
from AssetsServer.Server import *
from BackgroundTasks import *
settings = json.load(open('Settings.json'))
print('Welcome to Obiad Brawl. Running v1-2')
BackgroundTasks().start()
Networking().start()
if settings["UseUDPServer"]:
    UDPServer(host="0.0.0.0", port=5555).start()
if settings["gameAssetsServer"]:
    https_thread = Thread(target=Server.run)
    https_thread.start()