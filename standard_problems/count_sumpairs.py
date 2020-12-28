arr = [1,5,7,-1,5]
sum = 6
arr.sort()

def f(l=0,r=len(arr)-1):
    if l == r:
        return set()
    s = arr[l] + arr[r]
    if s > sum:
        return f(l,r-1)
    elif s < sum:
        return f(l+1,r)
    else:
        return {(l,r)}.union(f(l+1,r), f(l,r-1))


def twoPointer():
    result = f()
    pairs = []
    for (l,r) in result:
        pairs.append((arr[l],arr[r]))
    print(pairs)
    print(len(result))



twoPointer()
