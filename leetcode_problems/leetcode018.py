nums = [1,0,-1,0,-2,2]
target = 0
nums.sort()


def twoSum(arr,target):
    arr.sort()
    l, r = 0, len(arr)-1
    pairs = set()
    while l < r:
        s = arr[l] + arr[r]
        if s > target:
            r -= 1
        elif s < target:
            l += 1
        else:
            pairs.add((arr[l], arr[r]))
            l += 1
            r -= 1
    return pairs


def kSort(arr, target, k):
    sols = set()
    if k == 2: return twoSum(arr,target)

    for i in range(len(arr)):
        lower = kSort(arr[i+1:], target-arr[i], k-1)
        sols |= {tuple(list(x) + [arr[i]]) for x in lower}

    return sols

print(kSort(nums,target,4))
