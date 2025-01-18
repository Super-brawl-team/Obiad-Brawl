from Utils.Writer import Writer
from Entries.ChatStreamEntry import ChatStreamEntry
from Entries.JoinRequestAllianceStreamEntry import JoinRequestAllianceStreamEntry
from Entries.AllianceEventStreamEntry import AllianceEventStreamEntry
from Entries.ReplayStreamEntry import ReplayStreamEntry
from Entries.QuickChatStreamEntry import QuickChatStreamEntry
from Entries.TeamCreatedStreamEntry import TeamCreatedStreamEntry

class StreamEntryFactory:
    def createStreamEntryByType(ByteStream: Writer, message):
        v1 = message["EventType"]
        if v1 == 2:
            return ChatStreamEntry.encode(ByteStream, message)
        elif v1 == 3:
            return JoinRequestAllianceStreamEntry.encode(ByteStream, message)
        elif v1 == 4:
            return AllianceEventStreamEntry.encode(ByteStream, message)
        elif v1 == 5:
            return ReplayStreamEntry.encode(ByteStream, message)
        elif v1 == 8:
            return QuickChatStreamEntry.encode(ByteStream, message)
        elif v1 == 77:
            return TeamCreatedStreamEntry.encode(ByteStream, message)
        else:
            return None
        
        
         
    