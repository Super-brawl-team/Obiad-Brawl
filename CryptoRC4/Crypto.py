from Crypto.Cipher import ARC4 as RC4
import json


class CryptoRc4:

    def __init__(self):

        self.settings = json.load(open('Settings.json'))
        self.key = bytes(self.settings["RC4Key"], 'utf-8')
        print(f"[x] connection/deconnection using {self.key} key")
        self.nonce = b'nonce'
        self.RC4_Stream = RC4.new(self.key + self.nonce)
        self.RC4_Stream.encrypt(self.key + self.nonce)
        self.RC4_Stream2 = RC4.new(self.key + self.nonce)
        self.RC4_Stream2.encrypt(self.key + self.nonce)

    def decrypt(self, data):

        decryptedData = self.RC4_Stream.encrypt(data)
        return decryptedData

    def encrypt(self, data):

        encryptedData = self.RC4_Stream2.encrypt(data)
        return encryptedData
