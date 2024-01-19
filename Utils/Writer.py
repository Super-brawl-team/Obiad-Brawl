# -*- coding: utf-8 -*-

class Writer:
    
    def __init__(self, device):
        self.buffer = b''
        
    def size(self):
        return len(self.buffer)
    
    def getRaw(self):
        return self.buffer
    
    def getBuff(self):
        return self.buffer
    
    def writeIntEndian(self, data, length=4):
        self.buffer += data.to_bytes(length, 'little')
        
    def writeShortEndian(self, data, length=2):
        self.buffer += data.to_bytes(length, 'little')
        
    def writeInt8(self, data):
        self.writeInt(data, 1)
        
    def writeInt(self, data: int, length: int = 4):
        if data > 0:
            self.buffer += data.to_bytes(length, 'big', signed=False)
        else:
            self.buffer += data.to_bytes(length, 'big', signed=True)
            
    def writeByte(self, data):
        if data > 255:
            self.buffer += data.to_bytes(2, 'big', signed=False)
        elif data > 127:
            self.buffer += data.to_bytes(1, 'big', signed=False)
        else:
            self.buffer += data.to_bytes(1, 'big', signed=True)
            
    def writeLogicLong(self, data1, data2):
        self.writeVInt(data1)
        self.writeVInt(data2)
        
    def writeLong(self, data1, data2):
        self.writeInt(data1)
        self.writeInt(data2)
        
    def writeBytes(self, data):
        self.buffer += data
   
    def writeVint(self, data, rotate: bool = True):
        final = b''
        if data == 0:
            self.writeByte(0)
        elif data < 0:
            self.writeVInt((2147483648 * 2) + data)
        else:
            data = (data << 1) ^ (data >> 31)
            while data:
                b = data & 0x7f
                if data >= 0x80:
                    b |= 0x80
                if rotate:
                    rotate = False
                    lsb = b & 0x1
                    msb = (b & 0x80) >> 7
                    b >>= 1
                    b = b & ~0xC0
                    b = b | (msb << 7) | (lsb << 6)
                final += b.to_bytes(1, 'big')
                data >>= 7
            self.buffer += final   
            
    def writeVInt(self, data, rotate: bool = True):
        final = b''
        if data == 0:
            self.writeByte(0)
        elif data < 0:
            self.writeVInt((2147483648 * 2) + data)
        else:
            data = (data << 1) ^ (data >> 31)
            while data:
                b = data & 0x7f
                if data >= 0x80:
                    b |= 0x80
                if rotate:
                    rotate = False
                    lsb = b & 0x1
                    msb = (b & 0x80) >> 7
                    b >>= 1
                    b = b & ~0xC0
                    b = b | (msb << 7) | (lsb << 6)
                final += b.to_bytes(1, 'big')
                data >>= 7
            self.buffer += final
            
    def writeString(self, data=None):
        if data is not None:
            self.writeInt(len(data))
            self.buffer += data.encode('utf-8')
        else:
            self.writeInt(2**32 - 1)
            
    def writeHexa(self, data):
        if data:
            if data.startswith('0x'):
                data = data[2:]
            self.buffer += bytes.fromhex(''.join(data.split()).replace('-', ''))
            
    def writeScID(self, ClassID=0, InstanceID=0): # seriously? sc id? it's called data reference mr sroyzi
        # v3 = LogicData
        self.writeVInt(ClassID)
        if ClassID != 0:
            self.writeVInt(InstanceID)
            
    def writeScId(self, ClassID, InstanceID=0):
     # v3 = LogicData
        self.writeVInt(ClassID)
        if ClassID != 0:
            self.writeVInt(InstanceID)

            
    def writeBool(self, boolean: bool):
        if boolean:
            self.writeInt8(1)
        else:
            self.writeInt8(0)
            
    def writeArrayVInt(self, data):
        for x in data:
            self.writeVInt(x)
            
    def Send(self):
        self.encode()
        if hasattr(self, 'version'):
            self.device.SendData(self.id, self.buffer, self.version)
        else:
            self.device.SendData(self.id, self.buffer)
