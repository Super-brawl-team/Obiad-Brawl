from Utils.Writer import Writer
from Entries.StreamEntry import StreamEntry


class QuickChatStreamEntry:
    def encode(self: Writer, info):
        StreamEntry.encode(self, info)
        self.writeDataReference(40, info['MessageDataID'])
        self.writeBoolean(False)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(info['PremadeID'])