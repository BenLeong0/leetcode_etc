# DP(i,j) = DP(i-1,j) + DP(i,j-1)


def uniquePaths(m, n):
    # Set top-most row and left-most column to all one's
    number_of_routes = [[1 for _ in range(n)]] + [
        [1] + [0] * (n - 1) for _ in range(m - 1)
    ]

    # Dynamic Programming:
    # DP(i,j) = DP(i-1,j) + DP(i,j-1)
    for i in range(1, m):
        for j in range(1, n):
            number_of_routes[i][j] = (
                number_of_routes[i - 1][j] + number_of_routes[i][j - 1]
            )

    return number_of_routes[-1][-1]


print(uniquePaths(3, 7))
