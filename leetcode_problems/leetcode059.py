def generateMatrix(n):
    # Split up odd and even widths
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1, 2], [4, 3]]

    result = [[i for i in range(1, n + 1)]]
    rec = generateMatrix(n - 2)
    for i in range(n - 2):
        result.append(
            [4 * (n - 1) - i] + [x + 4 * (n - 1) for x in rec[i]] + [n + 1 + i]
        )
    result.append([i for i in range(2 * n - 1, 3 * n - 1)][::-1])
    return result


def f(m):
    for row in m:
        print(row)
    print("=========")


f(generateMatrix(1))
# [ [1] ]

f(generateMatrix(2))
# [ [1,2],
#   [4,3] ]

f(generateMatrix(3))
# [ [1,2,3],
#   [8,9,4],
#   [7,6,5] ]

f(generateMatrix(4))
# [ [01,02,03,04],
#   [12,13,14,05],
#   [11,16,15,06],
#   [10,09,08,07] ]

f(generateMatrix(5))
# [ [01,02,03,04,05],
#   [16,17,18,19,06],
#   [15,24,25,20,07],
#   [14,23,22,21,08],
#   [13,12,11,10,09] ]
