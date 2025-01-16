from Utils.Writer import Writer

class AllianceTeamEntry:
    
    def encode(ByteStream: Writer):
        ByteStream.writeVInt(1) # forgor
        ByteStream.writeBoolean(True) # hmm
        ByteStream.writeVInt(1) # forgor
        ByteStream.writeVInt(2) # forgor
        ByteStream.writeLong(0, 1) # room id
        ByteStream.writeVInt(1) # forgor
        ByteStream.writeVInt(2) # forgor
        ByteStream.writeDataReference(15, 2) # map
        ByteStream.writeVInt(0) # i shouldn't touch it apparently
        ByteStream.writeString("hi") # tf?
        ByteStream.writeLong(0, 1) # host id ?
        ByteStream.writeLong(0, 1) # host id?
        ByteStream.writeBoolean(True) # fuck is that
        ByteStream.writeBoolean(True) # fuck is that
        ByteStream.writeVInt(1) # players in this fucking damm team
        for x in range(1):
            ByteStream.writeLong(0, 1) # player id
        
        