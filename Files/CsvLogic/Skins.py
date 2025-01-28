import csv
from Files.CsvReader import CsvReader

class Skins:

    def getSkins(self):

        SkinsID = []

        with open('GameAssets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    SkinsID.append(line_count - 2)
                    line_count += 1

            return SkinsID
        
    def getBrawler(self, skinID):
        with open('GameAssets/csv_logic/skins.csv') as char_file:
            csv_reader = csv.reader(char_file, delimiter=',')
            skins = list(csv_reader)

        skins = skins[2:] 

        if skinID >= len(skins):
            return 0

        target = skins[skinID][1]
        with open('GameAssets/csv_logic/characters.csv') as card_file:
            csv_reader = csv.reader(card_file, delimiter=',')
            cards = list(csv_reader)
        cards = cards[2:]
        for index, row in enumerate(cards):
            if row[0] == target:
                return index
        return 0
    
    def getNonDefaultSkins(self):
        defaultSkins = []
        nonDefaultSkins = []
        with open('GameAssets/csv_logic/characters.csv') as card_file:
            csv_reader = csv.reader(card_file, delimiter=',')
            cards = list(csv_reader)
        cards = cards[2:]
        for index, row in enumerate(cards):
            defaultSkins.append(row[20])
        with open('GameAssets/csv_logic/skins.csv') as char_file:
            csv_reader = csv.reader(char_file, delimiter=',')
            skins = list(csv_reader)

        skins = skins[2:] 
        for index, row in enumerate(skins):
            if row[0] not in defaultSkins and row[1] != "":
                nonDefaultSkins.append(index)
        return nonDefaultSkins
    def getSkinPrice(self, skinID):
        with open('GameAssets/csv_logic/skins.csv') as char_file:
            csv_reader = csv.reader(char_file, delimiter=',')
            skins = list(csv_reader)

        skins = skins[2:] 

        if skinID >= len(skins):
            return 0

        price = skins[skinID][3]
        
        return price
    
    def getIsDefaultSkin(self, skinID):
        defaultSkins = []
        with open('GameAssets/csv_logic/characters.csv') as card_file:
            csv_reader = csv.reader(card_file, delimiter=',')
            cards = list(csv_reader)
        cards = cards[2:]
        for index, row in enumerate(cards):
            defaultSkins.append(row[20])
        with open('GameAssets/csv_logic/skins.csv') as char_file:
            csv_reader = csv.reader(char_file, delimiter=',')
            skins = list(csv_reader)

        skins = skins[2:] 

        if skinID >= len(skins):
            return 0

        name = skins[skinID][0]
        if name in defaultSkins:
            return True
        return False