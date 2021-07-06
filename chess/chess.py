import moves

empty_board = [[" " for _ in range(8)] for _ in range(8)]

start_board = (
    [["r", "n", "b", "q", "k", "b", "n", "r"], ["p" for _ in range(8)]]
    + [[" " for _ in range(8)] for _ in range(4)]
    + [[" " for _ in range(8)], ["R", "N", "B", "Q", "K", "B", "N", "R"]]
)

white_pieces = ["P", "R", "N", "B", "K", "Q"]
black_pieces = ["p", "r", "n", "b", "k", "q"]

ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]
files = ["8", "7", "6", "5", "4", "3", "2", "1"]

white_can_castle = {"short": True, "long": True}
black_can_castle = {"short": True, "long": True}


def get_white_moves(board):
    valid_moves = []
    switcher = {"P": lambda x, y, z: [], "N": []}
    for i in range(8):
        for j in range(8):
            switcher[board[i][j]](board, i, j)
    for (i, file) in enumerate(board):
        for (j, piece) in enumerate(file):
            if piece == "P":
                # Check if can move one square
                if board[i - 1][j] == " ":
                    valid_moves.append(f"{ranks[j]+files[i-1]}")

                # Check if can move two squares
                if i == 1:
                    if board[i - 1][j] == " " and board[i - 2][j] == " ":
                        valid_moves.append(f"{ranks[j]+files[i-2]}")

                # Check if can take
                if j > 0:
                    if board[i - 1][j - 1] in black_pieces:
                        valid_moves.append(f"{ranks[j]}x{ranks[j-1]+files[i-1]}")
                if j < 7:
                    if board[i - 1][j + 1] in black_pieces:
                        valid_moves.append(f"{ranks[j]}x{ranks[j+1]+files[i-1]}")

            elif piece == "N":
                for (x, y) in moves.get_knight_locations(i, j):
                    if board[x][y] == " ":
                        valid_moves.append(f"N{ranks[j]+files[i]}{ranks[y]+files[x]}")
                    elif board[x][y] in black_pieces:
                        valid_moves.append(f"N{ranks[j]+files[i]}x{ranks[y]+files[x]}")

            elif piece == "R":

                x = i + 1
                while x < 8:
                    if board[x][j] == " ":
                        valid_moves.append(f"R{ranks[j]+files[i]}{ranks[j]+files[x]}")
                    elif board[x][j] in black_pieces:
                        valid_moves.append(f"R{ranks[j]+files[i]}x{ranks[j]+files[x]}")
                        break
                    x += 1

                x = i - 1
                while x >= 0:
                    if board[x][j] == " ":
                        valid_moves.append(f"R{ranks[j]+files[i]}{ranks[j]+files[x]}")
                    elif board[x][j] in black_pieces:
                        valid_moves.append(f"R{ranks[j]+files[i]}x{ranks[j]+files[x]}")
                        break
                    x -= 1

                y = j + 1
                while y < 8:
                    if board[i][y] == " ":
                        valid_moves.append(f"R{ranks[y]+files[i]}{ranks[y]+files[i]}")
                    elif board[i][y] in black_pieces:
                        valid_moves.append(f"R{ranks[y]+files[i]}x{ranks[y]+files[i]}")
                        break
                    y += 1

                y = j - 1
                while y >= 0:
                    if board[i][y] == " ":
                        valid_moves.append(f"R{ranks[y]+files[i]}{ranks[y]+files[i]}")
                    elif board[i][y] in black_pieces:
                        valid_moves.append(f"R{ranks[y]+files[i]}x{ranks[y]+files[i]}")
                        break
                    y -= 1

            elif piece == "B":
                dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
                for (dx, dy) in dirs:
                    x, y = i + dx, j + dy
                    while 0 <= i + x < 8 and 0 <= j + y < 8:
                        if board[x][y] == " ":
                            valid_moves.append(
                                f"B{ranks[j]+files[i]}{ranks[y]+files[x]}"
                            )
                        elif board[x][y] in black_pieces:
                            valid_moves.append(
                                f"B{ranks[j]+files[i]}x{ranks[y]+files[x]}"
                            )
                            break
                        x += dx
                        y += dy

            elif piece == "K":
                dirs = [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]
                for (x, y) in dirs:
                    if 0 <= i + x < 8 and 0 <= j + y < 8:
                        if board[i + x][j + y] == " ":
                            valid_moves.append(
                                f"K{ranks[j]+files[i]}{ranks[j+y]+files[i+x]}"
                            )
                        elif board[i + x][j + y] in black_pieces:
                            valid_moves.append(
                                f"K{ranks[j]+files[i]}x{ranks[j+y]+files[i+x]}"
                            )

            elif piece == "Q":
                dirs = [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]
                for (dx, dy) in dirs:
                    x, y = dx, dy
                    while 0 <= i + x < 8 and 0 <= j + y < 8:
                        if board[i + x][j + y] == " ":
                            valid_moves.append(
                                f"Q{ranks[j]+files[i]}{ranks[j+y]+files[i+x]}"
                            )
                        elif board[i + x][j + y] in black_pieces:
                            valid_moves.append(
                                f"Q{ranks[j]+files[i]}x{ranks[j+y]+files[i+x]}"
                            )
                            break
                        x += dx
                        y += dy

    return valid_moves


print(get_white_moves(start_board))
for file in start_board:
    print(file)
