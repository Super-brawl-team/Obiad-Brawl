from Utils.Writer import Writer

class PlayerDisplayData:
    
    def encode(ByteStream: Writer, player):
        ByteStream.writeString("primoDEV") # player name
        ByteStream.writeInt(100) # player experience level
        ByteStream.writeInt(28000000) # player icon