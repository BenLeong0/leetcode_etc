import csv
import math


FILENAME ='data_numbers.csv'


def max_number_open(filename):
    with open(filename, 'r') as file:
        curr_line = file.readline()
        max_number = 0
        while curr_line:
            max_number = max(max_number, max([int(x) for x in curr_line.split(',')]))
            curr_line = file.readline()
    return max_number

print(max_number_open(FILENAME))


def max_number_csv(filename):
    f = open(filename)
    reader = csv.reader(f)
    return max([max(row) for row in reader])

print(max_number_csv(FILENAME))


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

print(max_row(FILENAME))
