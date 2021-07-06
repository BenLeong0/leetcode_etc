# DP(i,j) = DP(i-1,j) + DP(i,j-1)


def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid[-1][-1] == 1:
        return 0
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    # Set top-most row and left-most column to all one's, rest to zero
    number_of_routes = [[0] * n for _ in range(m)]

    # Set elements in home row to 1 unless any obstacles, after which leave as 0
    for i in range(m):
        if obstacleGrid[i][0] == 1:
            break
        else:
            number_of_routes[i][0] = 1

    # Set elements in home column to 1 unless any obstacles, after which leave as 0
    for j in range(n):
        if obstacleGrid[0][j] == 1:
            break
        else:
            number_of_routes[0][j] = 1

    # Dynamic Programming:
    # DP(i,j) = DP(i-1,j) + DP(i,j-1)
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                number_of_routes[i][j] = 0
            else:
                number_of_routes[i][j] = (
                    number_of_routes[i - 1][j] + number_of_routes[i][j - 1]
                )
    return number_of_routes[-1][-1]


print(uniquePathsWithObstacles([[0, 1], [0, 0]]))
