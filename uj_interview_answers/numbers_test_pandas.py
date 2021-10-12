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

csv_data = pd.read_csv("data_numbers.csv")
largest_row_sum = -float("inf")
for row in csv_data.iterrows():
    current_row_sum = row.sum(axis=1)
    if current_row_sum > largest_row_sum:
        largest_row_sum = current_row_sum
        largest_row = row
print(largest_row)
