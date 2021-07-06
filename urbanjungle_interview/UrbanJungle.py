import csv
import math


def sortNoDuplicates(s):
    s = set(s)
    s = list(s)
    s.sort()
    s = "".join(s)

    return s


def reverseOrder(s):
    s = s.split(" ")
    s = s[::-1]
    # s = " ".join(s)

    return s


def get_max_row(filename):
    with open(filename, newline="") as file:
        filereader = csv.reader(file, delimiter=",")
        # max_value = -math.inf
        # for row in filereader:
        #     max_value = max(max_value, max([int(x) for x in row]))

        max_sum = -math.inf
        curr_max_row = ""
        for row in filereader:
            row_sum = sum([int(value) for value in row])
            if row_sum > max_sum:
                max_sum = row_sum
                curr_max_row = ",".join(row)
        if not curr_max_row:
            raise ValueError("File is empty.")

    return curr_max_row


def find_tree(filename):
    tree_layout = []
    with open(filename, newline="") as file:
        filereader = csv.reader(file, delimiter=",")
        for row in filereader:
            tree_layout.append([int(tree) for tree in row])

    number_of_rows = len(tree_layout)

    a = 0
    for column_id in range(len(tree_layout[0])):  #
        column_min = math.inf
        for row_id in range(number_of_rows):
            column_min = min(column_min, tree_layout[row_id][column_id])
        a = max(a, column_min)

    b = 0
    for row in tree_layout:
        row_min = math.inf
        for tree in row:
            row_min = min(row_min, tree)
        b = max(b, row_min)

    # for row_id in range(len(tree_layout)):
    #     row_min = math.inf
    #     for column_id in range(len(tree_layout[0])):
    #         row_min = min(row_min, tree_layout[row_id][column_id])
    #     b = max(b, row_min)

    if a > b:
        return "a"
    elif b > a:
        return "b"
    else:
        return "same"


print(find_tree("xmas_trees.csv"))

# print(get_max_row("test.csv"))


s = "they mostly come at night. Mostly."
# print(sortNoDuplicates(s))
# print(reverseOrder(s))


# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

# deficient: <, perfect: =, abundant: >