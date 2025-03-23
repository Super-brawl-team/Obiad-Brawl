import csv
from time import perf_counter
from Files.CsvReader import CsvReader
from Files.CsvLogic.Characters import Characters

class Skills:


    def getSpecifiedSkillInfo(self, skill, info):

        with open('GameAssets/csv_logic/skills.csv', 'r') as csv_file:
                reader = csv.reader(csv_file)
                header = next(reader)
                index = header.index(info)
        with open('GameAssets/csv_logic/skills.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) 
            next(csv_reader) 
            for count, row in enumerate(csv_reader, start=1):
                if count == skill + 1:
                    information = row[index]
                    break
        return information     
