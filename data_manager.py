import csv
from community import Community
from voivodeship import Voivodeship
from county import County

class DataManager:

    @staticmethod
    def import_from_csv(filename):
        datatable = []
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)
            for row in reader:
                datatable.append(row)
        return datatable

    @classmethod
    def create_instances_from_data(cls, filename):
        data = cls.import_from_csv(filename)

        for row in data:
            if row[1] == '' and row[2] == '' and row[3] == '':
                wojewodztwo = Voivodeship(row[4], row[0])

            elif row[2] == "" and row[3] == "":
                powiat = County(row[4], row[1], row[5])

            else:
                gmina = Community(row[4], row[2], row[5], row[1])
