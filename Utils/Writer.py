# -*- coding: utf-8 -*-
from Utils.LogicLong import LogicLong
from Utils.Debugger import Debugger
from Utils.ByteStreamHelper import ByteStreamHelper
from Utils.ChecksumEncoder import ChecksumEncoder
from Utils.LogicStringUtil import LogicStringUtil
import zlib
from Utils.Helpers import Helpers

class Writer:
    
    def __init__(self, device):
        self.buffer = b''
        self.bitoffset = 0
        self.offset = 0
        self.checksum = 0
        self.length = len(self.buffer)
        
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

    def writeBytes(self, value, length = None):
        if length == None:
         try:
          length = len(value)
         except:
           length = 0
        ChecksumEncoder.writeBytes(self, value, length)
        self.bitoffset = 0
        if value != 0:
            Writer.writeIntToByteArray(self, length)
            self.buffer += value
            self.offset += length
        else:
            Writer.writeIntToByteArray(self, -1)
    def writeArrayVint(self, values):
        self.writeVInt(len(values))
        for x in values:
           self.writeVInt(x)
    def writeInt8(self, value):
        ChecksumEncoder.writeInt(self, value)
        self.bitoffset = 0
        tempBuf = list(self.buffer)
        tempBuf.append(value & 0xFF)
        self.buffer = bytes(tempBuf)
        self.offset += 1
    
    def writeInt16(self, value):
        ChecksumEncoder.writeInt(self, value)
        self.bitoffset = 0
        tempBuf = list(self.buffer)
        tempBuf.append(value >> 8 & 0xFF)
        tempBuf.append(value & 0xFF)
        self.buffer = bytes(tempBuf)
        self.offset += 2
        
    def writeInt24(self, value):
        ChecksumEncoder.writeInt(self, value)
        self.bitoffset = 0
        tempBuf = list(self.buffer)
        tempBuf.append(value >> 16 & 0xFF)
        tempBuf.append(value >> 8 & 0xFF)
        tempBuf.append(value & 0xFF)
        self.buffer = bytes(tempBuf)
        self.offset += 3
        
    def writeInt(self, value):
        ChecksumEncoder.writeInt(self, value)
        Writer.writeIntToByteArray(self, value)
        
    def writeIntLittleEndian(self, value):
        self.bitoffset = 0
        tempBuf = list(self.buffer)
        tempBuf.append(value & 0xFF)
        tempBuf.append(value >> 8 & 0xFF)
        tempBuf.append(value >> 16 & 0xFF)
        tempBuf.append(value >> 24 & 0xFF)
        self.buffer = bytes(tempBuf)
        self.offset += 4
        
    def writeIntToByteArray(self, value):
        self.bitoffset = 0
        tempBuf = list(self.buffer)
        tempBuf.append(value >> 24 & 0xFF)
        tempBuf.append(value >> 16 & 0xFF)
        tempBuf.append(value >> 8 & 0xFF)
        tempBuf.append(value & 0xFF)
        self.buffer = bytes(tempBuf)
        self.offset += 4
            
    def writeByte(self, value):
        ChecksumEncoder.writeByte(self, value)
        self.bitoffset = 0
        tempBuf = list(self.buffer)
        tempBuf.append(value & 0xFF)
        self.buffer = bytes(tempBuf)
        self.offset += 1
            
    def writeShort(self, value):
        ChecksumEncoder.writeShort(self, value)
        self.bitoffset = 0
        tempBuf = list(self.buffer)
        tempBuf.append(value >> 8 & 0xFF)
        tempBuf.append(value & 0xFF)
        self.buffer = bytes(tempBuf)
        self.offset += 2
    
    def writeLongLong(self, longlong):
        ChecksumEncoder.writeLongLong(self, longlong)
        self.bitoffset = 0
        high = LogicLong.getHigherInt(longlong)
        Writer.writeIntToByteArray(self, high)
        low = LogicLong.getLowerInt(longlong)
        Writer.writeIntToByteArray(self, low)

    def writeLong(self, high, low):
        self.writeIntToByteArray(high)
        self.writeIntToByteArray(low)
   
    def writeVint(self, data):
        self.bitoffset = 0
        if type(data) == str:
            data = int(data)
        final = b''
        if (data & 2147483648) != 0:
            if data >= -63:
                final += (data & 0x3F | 0x40).to_bytes(1, 'big', signed=False)
                self.offset += 1
            elif data >= -8191:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 2
            elif data >= -1048575:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 3
            elif data >= -134217727:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 4
            else:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 27) & 0xF).to_bytes(1, 'big', signed=False)
                self.offset += 5
        else:
            if data <= 63:
                final += (data & 0x3F).to_bytes(1, 'big', signed=False)
                self.offset += 1
            elif data <= 8191:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 2
            elif data <= 1048575:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 3
            elif data <= 134217727:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 4
            else:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 27) & 0xF).to_bytes(1, 'big', signed=False)
                self.offset += 5

        self.buffer += final  
            
    def writeVInt(self, data):
        self.bitoffset = 0
        if type(data) == str:
            data = int(data)
        final = b''
        if (data & 2147483648) != 0:
            if data >= -63:
                final += (data & 0x3F | 0x40).to_bytes(1, 'big', signed=False)
                self.offset += 1
            elif data >= -8191:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 2
            elif data >= -1048575:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 3
            elif data >= -134217727:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 4
            else:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 27) & 0xF).to_bytes(1, 'big', signed=False)
                self.offset += 5
        else:
            if data <= 63:
                final += (data & 0x3F).to_bytes(1, 'big', signed=False)
                self.offset += 1
            elif data <= 8191:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 2
            elif data <= 1048575:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 3
            elif data <= 134217727:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 4
            else:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 27) & 0xF).to_bytes(1, 'big', signed=False)
                self.offset += 5

        self.buffer += final
            
    def writeString(self, value=None):
        ChecksumEncoder.writeString(self, value)
        self.bitoffset = 0
        if value != None:
            str_bytes = LogicStringUtil.getBytes(value)
            str_length = LogicStringUtil.getByteLength(str_bytes)
            if str_length < 900001:
                Writer.writeIntToByteArray(self, str_length)
                self.buffer += str_bytes
                self.offset += str_length
            else:
                Debugger.warning(f"ByteStream::writeString invalid string length {str_length}")
                Writer.writeIntToByteArray(self, -1)
        else:
            Writer.writeIntToByteArray(self, -1)
            
    def writeHexa(self, data, length):
        self.bitoffset = 0
        if data:
            if data.startswith('0x'):
                data = data[2:]

            self.buffer += bytes.fromhex(''.join(data.split()).replace('-', ''))
            self.offset += length
            
    def writeDataReference(self, high=0, low=-1):
        ByteStreamHelper.writeDataReference(self, high, low)  
        
    def writeStringReference(self, value):
        ChecksumEncoder.writeStringReference(self, value)
        self.bitoffset = 0
        str_bytes = LogicStringUtil.getBytes(value)
        str_length = LogicStringUtil.getByteLength(str_bytes)
        if str_length < 900001:
            Writer.writeIntToByteArray(self, str_length)
            self.buffer += str_bytes
            self.offset += str_length
        else:
            Debugger.warning(f"ByteStream::writeString invalid string length {str_length}")
            Writer.writeIntToByteArray(self, -1)
            
    def writeScID(self, high=0, low=-1):
        ByteStreamHelper.writeDataReference(self, high, low)  
            
    def writeScId(self, high=0, low=-1):
        ByteStreamHelper.writeDataReference(self, high, low)  
    #def  writePackedBoolean(self, data):
        #v5 = 0
        #v6 = 0
        #v7 = 0
        #v8 = 0
        #v9 = 0
        #v10 = 0
        #v11 = 0
        #v12 = 0
        #ChecksumEncoder.writePackedBoolean(self, data)
        #if self.buffer:
           #if data:
             
    def writeBoolean(self, value):
        ChecksumEncoder.writeBoolean(self, value & 1)
        tempBuf = list(self.buffer)
        if self.bitoffset == 0:
            offset = self.offset
            self.offset += 1
            tempBuf.append(0)
        if (value & 1) != 0:
            tempBuf[self.offset - 1] = tempBuf[self.offset - 1] | 1 << (self.bitoffset & 31)
        self.bitoffset = self.bitoffset + 1 & 7
        self.buffer = bytes(tempBuf)
            
    def writeBool(self, value):
        ChecksumEncoder.writeBoolean(self, value & 1)
        tempBuf = list(self.buffer)
        if self.bitoffset == 0:
            offset = self.offset
            self.offset += 1
            tempBuf.append(0)
        if (value & 1) != 0:
            tempBuf[self.offset - 1] = tempBuf[self.offset - 1] | 1 << (self.bitoffset & 31)
        self.bitoffset = self.bitoffset + 1 & 7
        self.buffer = bytes(tempBuf)
            
    def writeArrayVInt(self, data):
        for x in data:
            self.writeVInt(x)
    
    def writeVLong(self, high, low):
        ChecksumEncoder.writeVLong(self, high, low)
        self.bitoffset = 0
        self.writeVInt(high)
        self.writeVInt(low)

    def writeCompressedString(self, data):
        self.bitoffset = 0
        compressedText = zlib.compress(data)
        self.writeInt(len(compressedText) + 4)
        self.writeIntLittleEndian(len(data))
        self.buffer += compressedText
        
    def encodeIntList(self, intList):
        ByteStreamHelper.encodeIntList(self, intList)
    
    def encodeLogicLong(self, logicLong):
        ByteStreamHelper.encodeLogicLong(self, logicLong)
        
    def writeLogicLong(self, high, low):
        self.writeVLong(high, low)
    
    def encodeLogicLongList(self, logicLongList):
        ByteStreamHelper.encodeLogicLongList(self, logicLongList)
     
    def Send(self):

        self.encode()
        if hasattr(self, 'version'):
            self.device.SendData(self.id, self.buffer, self.version)

        else:
            self.device.SendData(self.id, self.buffer)
        
        #print('[*] {} sent'.format(self.id))
    def SendTo(self, target):
        self.encode()
        if hasattr(self, 'version'):
            self.device.SendDataTo(self.id, self.buffer, target, self.version)

        else:
            self.device.SendDataTo(self.id, self.buffer, target)
    def SendUdp(self, target, client_address):
        self.encode()
        if hasattr(self, 'version'):
            self.device.SendDataUdp(self.id, self.buffer, target, client_address, self.version)

        else:
            self.device.SendDataUdp(self.id, self.buffer, target, client_address)


