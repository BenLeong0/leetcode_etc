from math import inf

ar1 = [1, 4, 5, 7]
ar2 = [10, 20, 30, 40]
x = 46


def twoSumMerge(ar1=ar1, ar2=ar2, x=x):
    inAr1 = []
    merged = []
    while ar1 and ar2:
        if ar1[0] < ar2[0]:
            merged.append(ar1.pop(0))
            inAr1.append(True)
        else:
            merged.append(ar2.pop(0))
            inAr1.append(False)
    inAr1 += [True for a in ar1] + [False for a in ar2]
    merged += ar1 + ar2

    l, r = 0, len(merged)-1
    diff = inf
    output = (0,0)
    while l != r:
        y = merged[l] + merged[r]
        if (inAr1[l] + inAr1[r]) % 2:       # XOR
            if abs(y-x) < diff:
                diff = abs(y-x)
                output = (merged[l], merged[r])
        if y > x:
            r -= 1
        else:
            l += 1

    return print(output)


def twoSumUnmerged(ar1=ar1, ar2=ar2, x=x):
    m,n = len(ar1), len(ar2)
    l, r = 0, n-1
    diff = inf
    output = (0,0)
    while l < m and r > 0:
        y = ar1[l] + ar2[r]
        if abs(y-x) < diff:
            diff = abs(y-x)
            output = (ar1[l], ar2[r])
        if y > x:
            r -= 1
        else:
            l += 1

    return print(output)



twoSumUnmerged()
