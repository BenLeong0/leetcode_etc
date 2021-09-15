import pandas as pd
from pandas.errors import EmptyDataError


def max_number(filename: str):
    try:
        df = pd.read_csv(filename, header=None)
        return df.max().max()
    except EmptyDataError:
        print(">> File is empty!")
        return None


def max_row(filename: str):
    try:
        df = pd.read_csv(filename, header=None)
        return ','.join(map(str,max(map(lambda row:row[1], df.iterrows()), key=lambda row:sum(row.values))))
    except EmptyDataError:
        print(">> File is empty!")
        return None



print(max_number("data_numbers.csv"))
print(max_number("blank.csv"))

print(max_row("data_numbers.csv"))
print(max_row("blank.csv"))
