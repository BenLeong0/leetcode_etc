def get_knight_locations(i, j):
    moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]

    return [(i + x, j + y) for (x, y) in moves if _is_position_within_bounds(x + i, y + j)]


def _is_position_within_bounds(x: int, y: int) -> bool:
    return 0 <= x <= 7 and 0 <= y <= 7
