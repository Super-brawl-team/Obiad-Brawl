import json

class Utility:
    def parseFields(fields: dict):
        print()
        for typeName,value in fields.items():
            print(f"{typeName}: {value}")
        print()
        
    def getFingerprintData(resourceSha):
        return json.dumps(json.loads(open(f"AssetsServer/Update/{resourceSha}/fingerprint.json", 'r').read()))