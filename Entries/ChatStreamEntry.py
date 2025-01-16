from Utils.Writer import Writer
from Entries.StreamEntry import StreamEntry


class ChatStreamEntry:
    def encode(ByteStream: Writer, info):
        StreamEntry.encode(ByteStream, info)
        ByteStream.writeString(info['Message'])