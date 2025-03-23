import os
import socket
import argparse
import copy
from threading import *
from Networking import *
from battle import *
import json
settings = json.load(open('Settings.json'))
print('Welcome to Obiad Brawl. Running v1-2')
Networking().start()
if settings["UseUDPServer"]:
    UDPServer(host="0.0.0.0", port=5555).start()