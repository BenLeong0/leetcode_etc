codes = [('I','V','X'),('X','L','C'),('C','D','M'),('M')]

def digit(n,level=0):
    if 0<=n<=3:
        return codes[level][0]*n
    elif n==4:
        return codes[level][0] + codes[level][1]
    elif n==9:
        return codes[level][0] + codes[level][2]
    else:
        return codes[level][1] + codes[level][0]*(n-5)

level = 3
result = ''
while level >= 0:
    result += digit(int(num/10**level),level)
    num %= 10**level
    level -= 1

print(result)
