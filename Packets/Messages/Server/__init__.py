__all__ = []

import pkgutil
import inspect


'''
Little script that load every messages in the directory:
    - just call : from Packets.Messages.Client import *
    and every packets class will be callable (e.g: LoginOk() )

'''
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    import importlib
    module = importlib.import_module(f'Packets.Messages.Server.{name}')
    for name, value in inspect.getmembers(module):
        if name.startswith('__'):
            continue

        globals()[name] = value
        __all__.append(name)
