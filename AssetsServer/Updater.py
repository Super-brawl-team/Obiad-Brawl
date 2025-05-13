import datetime
import http.server
import socket
import socketserver
import hashlib
import json
import os
import shutil

def getFileData(name, sha):
    return {'file': name, "sha": sha}

def generateHash(source):
    return hashlib.sha1(source).hexdigest()

fingeprintHash = generateHash(datetime.datetime.timestamp(datetime.datetime.now()).__str__().encode())
lastVersionFile = open("AssetsServer/lastversion.txt", "r").read()
version = lastVersionFile.split('.')
fingerprintData = {"files": [], "sha": fingeprintHash, "version": f'{version[0]}.{str(int(version[1]) + 1)}.{version[2]}'}

f = []
for (dirpath, dirnames, filenames) in os.walk('AssetsServer\\Content\\assets'):
    for i in filenames:
        if i != "fingerprint.json":
            f.append(os.path.join(dirpath, i))

os.mkdir(f"AssetsServer/Update/{fingeprintHash}")

newPath = f'AssetsServer/Update/{fingeprintHash}'
for i in f:
    fingerprintData['files'].append(getFileData(i.replace('AssetsServer\\Content\\assets\\', "").replace('\\', '\/'), generateHash(open(i, 'rb').read())))
    updatePath = i.replace('AssetsServer\\Content\\assets\\', "").replace('\\', '/').split("/")[0]
    if not os.path.exists(f'Update/{fingeprintHash}/{updatePath}'):
        os.mkdir(f'AssetsServer/Update/{fingeprintHash}/{updatePath}')
    shutil.copy(i, f'AssetsServer/Update/{fingeprintHash}/{updatePath}')

with open(f'AssetsServer/Update/{fingeprintHash}/fingerprint.json', 'w') as fingerprintFile:
    fingerprintFile.write(json.dumps(fingerprintData).replace('\\\\/', '\/'))
    fingerprintFile.close()

versionLast = open("AssetsServer/lastversion.txt", 'w+')
versionLast.write(f'{version[0]}.{str(int(version[1]) + 1)}.{version[2]}...{fingeprintHash}')
versionLast.close()