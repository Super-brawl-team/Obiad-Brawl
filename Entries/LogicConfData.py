from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
from Logic.Milestones import Milestones
from time import *

class LogicConfData:
    def encode(self: Writer, player):
        db = DataBase(player)
        self.player = player
        self.writeVInt(2017189)  # Shop Timestamp
        self.writeVInt(100) # box cost (gold)
        self.writeVInt(10) # box cost (gems)
        self.writeVInt(20) # Coin Boost cost
        self.writeVInt(50) # Coin Boost %
        self.writeVInt(50) # Coin Doubler cost
        self.writeVInt(1000) # Coin Doubled
        self.writeVInt(7*24) # Coin Boost Hours
        self.writeVInt(1) # default brawler chips
        self.writeVInt(2) # rare brawler chips
        self.writeVInt(10) # epic brawler chips
        self.writeVInt(60) # legendary brawler chips
        self.writeVInt(3) # default brawler cost
        self.writeVInt(10) # rare brawler cost
        self.writeVInt(70) # epic brawler
        self.writeVInt(600) # legendary brawler cost
		
        # Events array starts

        # Brawlers required for events starts

        self.writeVInt(self.player.eventCount) # count

        requiredBrawlers = [0, 3, 5, 8]

        for event in range(self.player.eventCount):
            self.writeVInt(event + 1) # event index
            self.writeVInt(requiredBrawlers[event]) # Brawlers needed for that

        # Brawlers required for events ends

        # disponible events starts
        eventData = db.loadEvents(1)["info"]["events"]
        self.writeVInt(len(eventData)) # disponibles event slot
        index = 0
        for event in eventData:
            events = eventData[event]
            self.writeVInt(index + 1) # slot index
            self.writeVInt(index + 1) # slot number
            self.writeVInt(events["TimeStamp"] - int(time())) # comming soon timer
            self.writeVInt(events["TimeStamp"] - int(time())) # Time Left
            self.writeVInt(events["Tokens"]) # coins to claim
            self.writeVInt(8) # bonuska coins
            self.writeVInt(999) # coins to win
            self.writeBoolean(False) # double coins
            self.writeBoolean(index == 3) # double exp
            self.writeScID(15, events["ID"]) # map
            self.writeVInt(0) #  coins already collected
            self.writeVInt(2) #  coins collected statut
            self.writeString("Server by PrimoDEVHacc") # text for event (TID) please keep it for credits
            if self.player.usedVersion >= 2:
                self.writeBoolean(False)
            index += 1

        # disponible events ends

        # comming soon events starts
        eventData = db.loadEvents(2)["info"]["events"]
        self.writeVInt(len(eventData)) # disponibles event slot
        index = 0
        for event in eventData:
            events = eventData[event]
            self.writeVInt(index + 1) # slot index
            self.writeVInt(index + 1) # slot number
            self.writeVInt(events["TimeStamp"] - int(time())) # comming soon timer
            self.writeVInt(events["TimeStamp"] - int(time())) # Time Left
            self.writeVInt(events["Tokens"]) # coins to claim
            self.writeVInt(8) # bonuska coins
            self.writeVInt(999) # coins to win
            self.writeBoolean(False) # double coins
            self.writeBoolean(index == 3) # double exp
            self.writeScID(15, events["ID"]) # map
            self.writeVInt(0) #  coins already collected
            self.writeVInt(2) #  coins collected statut
            self.writeString("Server by PrimoDEVHacc") # text for event (TID) please keep it for credits
            if self.player.usedVersion >= 2:
                self.writeBoolean(False)
            index += 1
        # comming soon event ends
            
        # Events array ends

        self.writeVInt(self.maximumUpgradeLevel) # upgrades Array
        for x in range(self.maximumUpgradeLevel):
            self.writeVInt(x + 1) # price

        Milestones.MilestonesArray(self)