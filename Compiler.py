import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import time

start_time = time.time()


class Compiler:
    @staticmethod
    def random_file():
        # setting the number of rows for the CSV file
        N = 5

        # creating a pandas dataframe (df) with 8 columns and N rows with random integers between 999 and 999999 and with column names from A to H
        df = pd.DataFrame(
            np.random.randint(999, 999999, size=(N, 7)), columns=list("ABCDEFG")
        )

        # creating one column 'H' of float type using the uniform distribution
        df["H"] = np.random.rand(N)

        # creating two additional columns with random strings
        df["I"] = pd.util.testing.rands_array(10, N)
        df["J"] = pd.util.testing.rands_array(10, N)

        # print the dataframe to see what we have created
        print(df)

        # export the dataframe to csv using comma delimiting
        df.to_csv("work.csv", sep=",")

    @staticmethod
    def random_to_sqlite():
        # E ==> Extract
        df = pd.read_csv("example_1M.csv")
        # print(df)

        # T ==> Transform
        csv_database = create_engine("sqlite:///csv_database.db")

        # L ==> Load
        df.to_sql("table1", csv_database)
        df = pd.read_sql_query("SELECT * FROM table1", csv_database)


# Compiler.random_file()
Compiler.random_to_sqlite()
print("--- %s seconds ---" % (time.time() - start_time))
