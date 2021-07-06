from math import factorial


def getPermutation(n, k):
    k -= 1
    result = []
    remaining_numbers = [i for i in range(n)]
    for i in range(n):
        index = k // factorial(n - i - 1)
        curr = remaining_numbers[index]
        del remaining_numbers[index]
        result.append(curr)
        k %= factorial(n - i - 1)
    return "".join([str(x + 1) for x in result])


print(getPermutation(3, 1))


# un = []
# 0...  <-  3! = 6
# 1...  <-  3! = 6  < (9-1)
# 2...  <-  3! = 6
# 3...  <-  3! = 6

# un = [1]
# 10... <- 2!
# 12... <- 2!  < 2  ((9-1)%6)
# 13... <- 2!

# un = [1,2]
# 1203    < 0 (((9-1)%6)%2)
# 1230