from Utils.Writer import Writer
from Entries.StreamEntry import StreamEntry

class MessageDataStreamEntry:
    def encode(self: Writer, info):
        StreamEntry.encode(self, info)
        self.writeDataReference(0, info["Tick"])

