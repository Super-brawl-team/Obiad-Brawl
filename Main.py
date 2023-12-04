import os
import socket
import argparse

from threading import *
from colorama import Fore, Style, init
from Networking import *
from TwistedNetworking import *

width = os.get_terminal_size().columns

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--debug', action='store_true', help='Will display DEBUG log messages.')
parser.add_argument('-t', '--twisted', action='store_true', help='Will use twisted framework instead of classic thread')

args = parser.parse_args()

init()

print('Welcome to my new project.'.center(width))

if args.twisted:
    startTwistedFactory()

else:
    Networking(args).start()
