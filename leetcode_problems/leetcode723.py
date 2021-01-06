"""
Candy crush simulator!!!!
https://just4once.gitbooks.io/leetcode-notes/content/.gitbook/assets/723.png
"""


board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]



height = len(board)
width = len(board[0])


check = True
while check:
    check = False
    for row in board:
        print(["{: 5d}".format(x) for x in row])
    print('====')

    # Find groups
    for i in range(height):
        for j in range(width):
            if i < height-2:
                if abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+2][j]):
                    board[i][j] = board[i+1][j] = board[i+2][j] = -abs(board[i][j])
            if j < width - 2:
                if abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]):
                    board[i][j] = board[i][j+1] = board[i][j+2] = -abs(board[i][j])

    # Crush the candy
    for i in range(height):
        for j in range(width):
            if board[i][j] < 0:
                for x in range(i,0,-1):
                    board[x][j] = board[x-1][j]
                board[0][j] = 0
                check = True
