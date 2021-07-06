# DP(i,j) = DP(i-1,j) + DP(i,j-1)


def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    # Set top-most row and left-most column to all one's, rest to zero
    shortest_routes = [[0] * n for _ in range(m)]

    # Dynamic Programming:
    # DP(i,j) = DP(i-1,j) + DP(i,j-1)
    for i in range(m):
        for j in range(n):
            if i == 0:  # Left-most column
                if j == 0:  # Top left square
                    shortest_routes[i][j] = grid[i][j]
                else:
                    shortest_routes[i][j] = grid[i][j] + shortest_routes[i][j - 1]
            elif j == 0:  # Top-most row
                shortest_routes[i][j] = grid[i][j] + shortest_routes[i - 1][j]
            else:  # Take shortest of route from above or left
                shortest_routes[i][j] = grid[i][j] + min(
                    shortest_routes[i][j - 1], shortest_routes[i - 1][j]
                )

    return shortest_routes[-1][-1]


print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
