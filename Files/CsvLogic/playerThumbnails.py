from Files.CsvReader import CsvReader
import csv

class playerThumbnails:
    def getAllThumbnails(self):

        thumbnailsID = []

        with open('GameAssets/csv_logic/player_thumbnails.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    thumbnailsID.append(line_count - 2)
                    line_count += 1

            return thumbnailsID
    def getRequiredTrophiesForThumbnail(self, ID):
        with open('GameAssets/csv_logic/player_thumbnails.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) 
            next(csv_reader)
            line_count = 0
            for row in csv_reader:
                  
                  if line_count == ID:
                    requiredTrophies = row[2]
                    break
                  line_count += 1

            return int(requiredTrophies)
        
    def getRequiredExpForThumbnail(self, ID):
        with open('GameAssets/csv_logic/player_thumbnails.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) 
            next(csv_reader)
            line_count = 0
            for row in csv_reader:
                  
                  if line_count == ID:
                    requiredBrawler = row[1]
                    break
                  line_count += 1

            return int(requiredBrawler)

    def getRequiredBrawlerForThumbnail(self, ID):
        with open('GameAssets/csv_logic/player_thumbnails.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) 
            next(csv_reader)
            requiredBrawler = None
            line_count = 0
            for row in csv_reader:
                  
                  if line_count == ID:
                    requiredBrawler = row[3]
                    break
                  line_count += 1
            if requiredBrawler == None:
                requiredBrawler = 0
            return requiredBrawler