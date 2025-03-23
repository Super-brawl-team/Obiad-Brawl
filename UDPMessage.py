from Packets.PiranhaMessage import PiranhaMessage
from Utils.ByteStream import ByteStream
import asyncio
from Logic.Device import Device
class UDPMessage:
    def __init__(self, socket, udpSessionID, addr):
        self.byteStream: ByteStream = None
        self.socket: asyncio.DatagramTransport = socket
        self.udpSessionID: bytes = udpSessionID
        self.addr = addr
        self.device = Device()

    def encodeMessage(self, message: PiranhaMessage, id, device):
        self.buffer = message.encode()
        #print(self.buffer)
        stream = ByteStream(b"")
        stream.writeBytesWithoutLength(b'0123456789', 10)
        stream.writeVInt(id)
        self.buffer = device.crypto.encrypt(self.buffer)
        stream.writeVInt(len(self.buffer))
        stream.writeBytesWithoutLength(self.buffer, len(self.buffer))
        self.byteStream = stream
        print(str(id) + "created")
        return self.byteStream
    def decodeMessage(self, message: PiranhaMessage):
        #message.decode({"smack": "gok"})
        fields = {}
        stream = ByteStream(message)
        fields["sessionToken"] = stream.readBytes(10)
        fields["messageType"] = stream.readVInt()
        fields["messageLenght"] = stream.readVInt()
        fields["payload"] = stream.readBytes(fields["messageLenght"])
        return fields
        
    
    def send(self, byteStream):
        self.socket.sendto(byteStream.messagePayload, self.addr)