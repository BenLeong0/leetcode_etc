"""
With the file 'data_numbers.csv':

1) Return the largest number in a csv given the filename

2) Return the row with the largest sum in a csv given the filename.
"""

import csv
import math


FILENAME = 'data_numbers.csv'
MAX_NUM = 999975
MAX_ROW = ['543563', '857430', '452612', '704294', '580649', '727532', '966768', '-325715', '171569', '580695']


# Natural approach

def max_number(filename):
    with open(filename, 'r') as file:
        curr_line = file.readline()
        if not curr_line:
            raise ValueError(f"Empty file {filename}")
        max_number = -math.inf
        while curr_line:
            max_number = max(max_number, max([int(x) for x in curr_line.split(',')]))
            curr_line = file.readline()
    return max_number

assert max_number(FILENAME) == MAX_NUM
print("max_number successful!")


def max_row(filename):
    largest_sum = None
    largest_row = []

    file = open(filename)
    reader = csv.reader(file)
    for line in reader:
        # Can use either method below to parse line
        parsed_line = [int(x) for x in line]
        parsed_line = map(int, line)
        line_sum = sum(parsed_line)

        if largest_sum is None or line_sum > largest_sum:
            largest_sum = line_sum
            largest_row = line

    return largest_row

assert max_row(FILENAME) == MAX_ROW
print("max_row successful!")


# CULTURA MÁXIMA

def max_number_csv(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        return max([max(map(int, row)) for row in reader])
    # return max([max(map(int, row)) for row in csv.reader(open(filename))])

assert max_number_csv(FILENAME) == MAX_NUM
print("max_number_csv successful!")


def max_row_comprehension(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        return max(reader, key=lambda line: sum(map(int, line)))
    # return max(csv.reader(open(filename)), key=lambda line: sum(map(int, line)))

assert max_row_comprehension(FILENAME) == MAX_ROW
print("max_row_comprehension successful!")
