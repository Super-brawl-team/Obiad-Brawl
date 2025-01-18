import io
import random

class RC4Encrypter:
    def __init__(self, key):
        if not isinstance(key, bytes):
            key = key.encode()
        self._box = list(range(256))
        j = 0
        for i in range(256):
            j = (j + self._box[i] + key[i % len(key)]) % 256
            self._box[i], self._box[j] = self._box[j], self._box[i]
        self._i = 0
        self._j = 0

    def update(self, msg):
        if not isinstance(msg, bytes):
            msg = msg.encode()
        box = self._box
        i = self._i
        j = self._j
        out = bytearray(len(msg))
        for k in range(len(msg)):
            i = (i + 1) % 256
            j = (j + box[i]) % 256
            box[i], box[j] = box[j], box[i]
            out[k] = msg[k] ^ box[(box[i] + box[j]) % 256]
        self._i = i
        self._j = j
        return out

    def skip(self, n):
        box = self._box
        i = self._i
        j = self._j
        for _ in range(n):
            i = (i + 1) % 256
            j = (j + box[i]) % 256
            box[i], box[j] = box[j], box[i]
        self._i = i
        self._j = j

class RC4Transform(io.BufferedIOBase):
    def __init__(self, key):
        self._rc4 = RC4Encrypter(key)

    def _transform(self, data):
        if data:
            return self._rc4.update(data)
        return b''

    def read(self, size=-1):
        return self._transform(super().read(size))

    def write(self, b):
        return len(self._transform(b))

    def skip(self, n):
        self._rc4.skip(n)

RC4Encrypter.Transform = RC4Transform