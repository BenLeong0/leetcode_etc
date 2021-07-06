def get_knight_locations(i, j):
    moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]

    return [(i + x, j + y) for (x, y) in moves if (0 <= i + x <= 7 and 0 <= j + y <= 7)]
