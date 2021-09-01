import csv
import math


FILENAME = 'data_numbers.csv'
MAX_NUM = 999975
MAX_ROW = ['543563', '857430', '452612', '704294', '580649', '727532', '966768', '-325715', '171569', '580695']


def max_number_open(filename):
    with open(filename, 'r') as file:
        curr_line = file.readline()
        max_number = 0
        while curr_line:
            max_number = max(max_number, max([int(x) for x in curr_line.split(',')]))
            curr_line = file.readline()
    return max_number

assert max_number_open(FILENAME) == MAX_NUM


def max_number_csv(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        return max([max(map(int, row)) for row in reader])

assert max_number_csv(FILENAME) == MAX_NUM


def max_row(filename):
    largest_sum = -math.inf
    largest_row = []

    file = open(filename)
    reader = csv.reader(file)
    for line in reader:
        # Can use either method below to parse line
        parsed_line = [int(x) for x in line]
        parsed_line = list(map(int, line))

        if sum(parsed_line) > largest_sum:
            largest_sum = sum(parsed_line)
            largest_row = line

    return largest_row

max_row(FILENAME) == MAX_ROW


def max_row_comprehension(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        return max(reader, key=lambda line: sum(map(int, line)))

max_row_comprehension(FILENAME) == MAX_ROW
