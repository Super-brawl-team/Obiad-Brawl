import csv
from time import perf_counter
from Files.CsvReader import CsvReader
from Files.CsvLogic.Characters import Characters

class Cards:


    def getCards(self):

        CardsID = []

        with open('GameAssets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    CardsID.append(line_count - 2)
                    line_count += 1

            return CardsID

    def getBrawlerRarity(self, ID):
        brawler_rarity = None 
        with open('GameAssets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) 
            next(csv_reader) 
            for count, row in enumerate(csv_reader, start=1):
                if count == ID + 1:
                    brawler_rarity = row[10]
                    break
        return brawler_rarity
    def getUnlock(self, card):
        brawler = None
        with open('GameAssets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) 
            next(csv_reader)
            for count, row in enumerate(csv_reader, start=0):
                if count == card:
                    brawler = row[3]
                    if row[5] == 'unlock':
                        return count
                    break

            csv_file.seek(0)
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) 
            next(csv_reader) 

            for count, row in enumerate(csv_reader, start=0):
                if row[3] == brawler and row[5] == 'unlock':
                    return count

        return None
    def isUnlock(self, ID):
        with open('GameAssets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) 
            next(csv_reader) 
            for count, row in enumerate(csv_reader, start=0):
                if count == ID:
                    if row[5] == "unlock":
                        return True
                    
                    return False
        return False
    
    def getbrawlerID(self, card):
        brawler = None
        with open('GameAssets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) 
            next(csv_reader)
            for count, row in enumerate(csv_reader, start=0):
                if count == card:
                    brawler = row[3]
                    break
            return Characters().getCharacterByName(brawler)
        
    
    def getBrawlers(self):
        BrawlersID = []

        with open('GameAssets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[5] == 'unlock':
                        if not Characters().isDisabled(row[3]):
                          BrawlersID.append(line_count - 2)
                    line_count += 1

            return BrawlersID
    