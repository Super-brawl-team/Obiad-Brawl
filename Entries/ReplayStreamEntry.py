from Utils.Writer import Writer
from Entries.StreamEntry import StreamEntry


class ReplayStreamEntry:
    def encode(self: Writer, info):
        StreamEntry.encode(self, info)
        self.writeVInt(0)
        self.writeLong(0, 1)
        self.writeBoolean(False)
        self.writeString("String1")
        self.writeString("String2")
        self.writeString("String3")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

