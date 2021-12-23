import petl as etl

# import csv

# fileName = "csv_database.db"


# class PETL:
#     @staticmethod
#     def extract():
#         print(open(fileName).read())


# PETL.extract()
# ================= JSONS Files =================#
import petl as etl

data = """
    [{"foo": "a", "bar": 1},
    {"foo": "b", "bar": 2},
    {"foo": "c", "bar": 2}]
    """
with open("example.json", "w") as f:
    f.write(data)

table1 = etl.fromjson("example.json", header=["foo", "bar"])
print(table1)

# ================= JSONS Files ================= #
import petl as etl

table1 = [["foo", "bar"], ["a", 1], ["b", 2], ["c", 2]]
etl.tohtml(table1, "example.html", caption="example table")
print(open("example.html").read())


# ================= Pandas DataFrame Files =================#
import petl as etl
import pandas as pd

records = [("apples", 1, 2.5), ("oranges", 3, 4.4), ("pears", 7, 0.1)]
df = pd.DataFrame.from_records(records, columns=("foo", "bar", "baz"))
table = etl.fromdataframe(df)
print(table)

# ================= To CSV ================= #
from petl import tocsv, look

tocsv(table, "test.csv")
tocsv("extract from", "load into")

# ================= Appand CSV ================= # MERGE
from petl import appendcsv

appendcsv(table, "test.csv")
appendcsv("extract from", "load into")

# ================= Appand pickle ================= #
from petl import topickle, look

topickle(table, "test.dat")
topickle("extract from", "load into")
