import zlib

from io import BufferedReader, BytesIO


class ByteStream(BufferedReader):
    def __init__(self, initial_bytes):
        super().__init__(BytesIO(initial_bytes))
        self.buffer = b'' 
        self.payload = self.buffer
        self.offset = 0
        self.bitoffset = 0

    def readByte(self):
        return int.from_bytes(self.read(1), "big")

    def readDataReference(self):
      Data = {}
      Data["High"] = self.readVInt()
      if Data["High"] == 0:
        return Data["High"], 0
      else:
        Data["Low"] = self.readVInt()
        return Data["High"], Data["Low"]
   
    def readUint32(self, length=4):
        return int.from_bytes(self.read(length), "big")
    
    def readCommandHeader(self):
        for x in range(9):
            self.readVInt()
    
    def readVInt(self):
        n = self.readVariableInt(True)
        return (n >> 1) ^ (-(n & 1))

    def readBoolean(self):
        result = bool.from_bytes(bytes=self.read(1), byteorder='big', signed=False)
        if result == True:
            return True
        else:
            return False
    
    def readShort(self, length=2):
        return int.from_bytes(self.read(length), "big")

    def readInt(self, length=4):
        return int.from_bytes(self.read(length), "big")

    def readVariableInt(self, rotate: bool = True):
        result = 0
        shift = 0
        while True:
            byte = self.readByte()
            if rotate and shift == 0:
                seventh = (byte & 0x40) >> 6  # save 7th bit
                msb = (byte & 0x80) >> 7  # save msb
                n = byte << 1  # rotate to the left
                n = n & ~0x181  # clear 8th and 1st bit and 9th if any
                byte = n | (msb << 7) | seventh  # insert msb and 6th back in
            result |= (byte & 0x7f) << shift
            shift += 7
            if not (byte & 0x80):
                break
        return result


    def readLong(self):
        result = []
        result.append(self.readInt())
        result.append(self.readInt())
        return result
    
    def readString(self):
        length = self.readInt()
        if length == pow(2, 32) - 1:
            return b""
        else:
            try:
                decoded = self.read(length)
            except MemoryError:
                raise IndexError("String out of range.")
            else:
                return decoded.decode('utf-8')


    
    def peekInt(self, length=4):
        return int.from_bytes(self.peek(length)[:length], "big")

    
