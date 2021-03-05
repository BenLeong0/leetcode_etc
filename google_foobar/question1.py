from math import sqrt

def solution(i):
    primes = []
    primeLength = 0

    def isPrime(n):
        for prime in primes:
            if n % prime == 0:
                return False
            if prime > sqrt(n):
                break
        return True

    n = 2
    while primeLength < i+5:
        if isPrime(n):
            primeLength += len(str(n))
            primes.append(n)
        n += 1

    primeString = ''.join([str(x) for x in primes])
    print(primeString)
    return int(primeString[i:i+5])

print(solution(0))
