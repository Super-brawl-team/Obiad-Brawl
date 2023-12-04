__all__ = []

import pkgutil
import inspect


'''
Little script that load every messages in the directory:
    - just call : from Packets.Messages.Client import *
    and every packets class will be callable (e.g: ClientHello() )

'''
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)

    for name, value in inspect.getmembers(module):
        if name.startswith('__'):
            continue

        globals()[name] = value
        __all__.append(name)
