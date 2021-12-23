import petl as etl
import csv

fileName = "csv_database.db"


class PETL:
    @staticmethod
    def extract():
        print(open(fileName).read())


PETL.extract()
