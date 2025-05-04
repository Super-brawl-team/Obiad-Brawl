from Utils.Writer import Writer
from Entries.StreamEntry import StreamEntry


class TeamCreatedStreamEntry:
    def encode(self: Writer, info):
        StreamEntry.encode(self, info)
        self.writeLong(0, info["promotedTeam"])
        self.writeVInt(0) # ad info tid id
        self.writeVInt(0) # unk
        self.writeVInt(0) # unk
