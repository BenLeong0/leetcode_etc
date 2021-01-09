from math import log

def isPalindromeSlow(x):
    # Runs in O(len(x))
    if x < 0:
        return False
    elif x%10 == 0 and x != 0:
        return False
    n = 1
    while x > 10**(n):
        n += 1
    for i in range(n//2):
        if x//(10**i)%10 != x//(10**(n-1-i))%10:
            return False
    return True


def isPalindrome(x):
    # Runs in O(log_10(len(x)))
    if x < 0:
        return False
    elif x%10 == 0 and x != 0:
        return False

    reversedNumber = 0
    while x > reversedNumber:
        reversedNumber = reversedNumber*10 + x%10
        x //= 10

    # compare to //10 in case odd number of digits
    return x == reversedNumber or x == reversedNumber//10




x = 1001
print(isPalindrome(x))
