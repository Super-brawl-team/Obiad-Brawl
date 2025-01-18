from tinydb import database
from Utils.Config import Config
from Core.Crypto import encrypt
from Utils.ChecksumEncoder import ChecksumEncoder


packet_settings = Config.GetValue()


class Writer:
    def __init__(self, client, endian: str = 'big'):
        self.client = client
        self.endian = endian
        self.buffer = b''
        self.bitoffset = 0
        self.result8 = 0
        self.offset = 0


    def writeIntEndian(self, data, length=4):
        self.buffer += data.to_bytes(length, 'little')
    
    def writeShortEndian(self, data, length=2):
        self.buffer += data.to_bytes(length, 'little')
        
    def size(self):
        return len(self.buffer)
    
    def getRaw(self):
        return self.buffer
        
    def writeInt2(self, data, length=4):
        self.buffer += data.to_bytes(length, 'big')


    def writeInt(self, value):
        v5 = 0
        v6 = 0
        v7 = 0
        v8 = 0
        data = b''
        data += ((value >> 24) & 0xFF).to_bytes(1, 'big', signed=False)
        data += ((value >> 16) & 0xFF).to_bytes(1, 'big', signed=False)
        data += ((value >> 8) & 0xFF).to_bytes(1, 'big', signed=False)
        data += (value & 0xFF).to_bytes(1, 'big', signed=False)
        self.buffer += data
    def writeUInteger(self, integer: int, length: int = 1):
        self.buffer += integer.to_bytes(length, self.endian, signed=False)


    def writeInt8(self, data):
        self.writeInt(data, 1)
    
    def writeLong(self, high, low):
        self.buffer += high.to_bytes(4, 'big') + low.to_bytes(4, 'big')


    def writeLogicLong(self, data1, data2):
        self.writeVint(data1)
        self.writeVint(data2)
    
    
    def writeArrayVint(self, data):
        self.writeVint(len(data))
        for x in data:
            self.writeVint(x)


    def writeUInt8(self, integer: int):
        self.writeUInteger(integer)


    
    

    def writeBool(self, boolean: bool):
        if boolean:
            self.writeUInt8(1)
        else:
            self.writeUInt8(0)
    
    def writeBoolean(self, boolean: bool):
        if boolean:
            self.writeUInt8(1)
        else:
            
           self.writeUInt8(0)
    
    def writeHexa(self, data):
        if data:
            if data.startswith('0x'):
                data = data[2:]
            self.buffer += bytes.fromhex(''.join(data.split()).replace('-', ''))


    def send(self):

        self.encode()
        if hasattr(self, 'version'):
            self.device.SendData(self.id, self.buffer, self.version)

        else:
            self.device.SendData(self.id, self.buffer)

    def sendToAll(self):
        if self.player.ClubID != 0:
            self.encode()
            packet = encrypt(self.buffer)
            self.buffer = self.id.to_bytes(2, 'big', signed=True)
            #self.writeInt(len(packet), 3)
            if hasattr(self, 'version'):
                self.writeInt16(self.version)
            else:
                self.writeInt16(0)
            self.buffer += packet
            for Client in range(self.player.ClientDict["ClientCounts"]):
                for client_id, value in self.player.ClientDict["Clients"].items():
                    DataBase.loadOtherAccount(self, int(client_id))
                    if self.ClubID == self.player.ClubID:
                        self.player.ClientDict["Clients"][str(client_id)]["SocketInfo"].send(self.buffer)
                break
            if packet_settings["ShowPacketsInLog"] == True:
                print(self.id, self.__class__.__name__)

    def sendToOthers(self):
        if self.player.ClubID != 0:
            self.encode()
            packet = encrypt(self.buffer)
            
            if hasattr(self, 'version'):
                self.device.SendData(self.id, self.buffer, self.version)
            else:
                self.device.SendData(self.id, self.buffer)
            #self.buffer += packet + b'\xff\xff\x00\x00\x00\x00\x00'
            for Client in range(self.player.ClientDict["ClientCounts"]):
                for client_id, value in self.player.ClientDict["Clients"].items():
                    DataBase.loadOtherAccount(self, int(client_id))
                    if client_id != self.player.LowID and self.ClubID == self.player.ClubID:
                        self.player.ClientDict["Clients"][str(client_id)]["SocketInfo"].send(self.buffer)
                break
            if packet_settings["ShowPacketsInLog"] == True:
                print(self.id, self.__class__.__name__)

    def sendWithLowID(self, low_id):
        #try:
            self.encode()
            #packet = encrypt(self.buffer)
            #self.buffer = self.id.to_bytes(2, 'big', signed=True)
            #self.writeInt(len(packet), 3)
            if hasattr(self, 'version'):
               for PlayerSocket in range(self.player.ClientDict["ClientCounts"]):
                self.device.SendDataToSomeoneElse(self.id, self.buffer, self.player.ClientDict["Clients"][str(low_id)]["SocketInfo"], self.version)
            else:
                for PlayerSocket in range(self.player.ClientDict["ClientCounts"]):
                    self.device.SendDataToSomeoneElse(self.id, self.buffer, self.player.ClientDict["Clients"][str(low_id)]["SocketInfo"])
            
        #except:
            #pass

            if packet_settings["ShowPacketsInLog"] == True:
              print(self.id, self.__class__.__name__)

        

    def writeVinte(self, data, rotate: bool = True):
        final = b''
        if data == 0:
            self.writeByte(0)
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

    def writeVInte(self, data, rotate: bool = True):
        final = b''
        if data == 0:
            self.writeByte(0)
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
    
    def writeVInt(self, value):
        v2 = value
        ChecksumEncoder.writeVInt(self, value)
        if type(value) == str:
            value == int(data)
            print("warning", "String Value on function ByteStream::writeVInt detected")
        self.bitoffset = 0
        data = b''

        if (v2 & 2147483648) != 0:
            if v2 >= -63:
                data += (v2 & 0x3F | 0x40).to_bytes(1, 'big', signed=False)      
                self.offset += 1
            elif v2 > -8192:
                data += (v2 & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F).to_bytes(1, 'big', signed=False) 
                self.offset += 2
            elif v2 > -1048576:
                data += (v2 & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 16) | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 3
            elif v2 > -134217727:
                data += (v2 & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 4
            else:
                data += (v2 & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 27) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 5
        
        else:
            if v2 <= 63:
                data += (v2 & 0x3F).to_bytes(1, 'big', signed=False)
                self.offset += 1
            elif v2 <= 0x2000:
                data += (v2 & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6 ) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 2
            elif v2 <= 0x100000:
                data += (v2 & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 3
            elif v2 <= 0x7FFFFFF:
                data += (v2 & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 4
            else:
                data += (v2 & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 27) & 0xF).to_bytes(1, 'big', signed=False)
                self.offset += 5
        
        self.buffer += data
    
    def writeVint(self, value):
        v2 = value
        ChecksumEncoder.writeVInt(self, value)
        if type(value) == str:
            value == int(data)
            Debugger.log("warning", "String Value on function ByteStream::writeVInt detected")
        self.bitoffset = 0
        data = b''

        if (v2 & 2147483648) != 0:
            if v2 >= -63:
                data += (v2 & 0x3F | 0x40).to_bytes(1, 'big', signed=False)      
                self.offset += 1
            elif v2 > -8192:
                data += (v2 & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F).to_bytes(1, 'big', signed=False) 
                self.offset += 2
            elif v2 > -1048576:
                data += (v2 & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 16) | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 3
            elif v2 > -134217727:
                data += (v2 & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 4
            else:
                data += (v2 & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 27) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 5
        
        else:
            if v2 <= 63:
                data += (v2 & 0x3F).to_bytes(1, 'big', signed=False)
                self.offset += 1
            elif v2 <= 0x2000:
                data += (v2 & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6 ) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 2
            elif v2 <= 0x100000:
                data += (v2 & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 3
            elif v2 <= 0x7FFFFFF:
                data += (v2 & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 4
            else:
                data += (v2 & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 27) & 0xF).to_bytes(1, 'big', signed=False)
                self.offset += 5
        
        self.buffer += data
        
    def writeString(self, string: str = None):
        if string is None:
            self.writeInt((2**32)-1)
        else:
            encoded = string.encode('utf-8')
            self.writeInt(len(encoded))
            self.buffer += encoded

    def writeIntToByteArray(self, value):
        self.bitoffset = 0
        tempBuf = list(self.buffer)
        tempBuf.append(value >> 24 & 0xFF)
        tempBuf.append(value >> 16 & 0xFF)
        tempBuf.append(value >> 8 & 0xFF)
        tempBuf.append(value & 0xFF)
        self.buffer = bytes(tempBuf)
        self.offset += 4

    def write_string_reference(self, string: str = None):

        encoded = string.encode('utf-8')
        self.writeInt16(0)
        self.writeVint(len(encoded))
        self.buffer += encoded

    def writeByte(self, data):
        ChecksumEncoder.writeByte(self, data)
        tempBuf = list(self.buffer)
        tempBuf.append(data & 0xFF)
        self.buffer = bytes(tempBuf)
    
    def writeBytes(self, value, length):
        ChecksumEncoder.writeBytes(self, value, length)
        self.bitoffset = 0
        if value != 0:
            Writer.writeIntToByteArray(self, length)
            self.buffer += value
            self.offset += length
        else:
            Writer.writeIntToByteArray(self, -1)

    def writeInt16(self, data):
        self.writeInt(data, 2)

    def writeScId(self, x, y):
        self.writeVint(x)
        self.writeVint(y)
        
    def writeScID(self, x, y):
        self.writeVint(x)
        self.writeVint(y)
    
    def writeDataReference(self, x, y):
        self.writeVint(x)
        self.writeVint(y)
        
        
    
    def writeNullVint(self):
        self.writeVint(-1)