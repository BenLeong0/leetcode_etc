import copy
from math import inf
from typing import List

FIRST_ARRAY = [1, 4, 5, 7]
SECOND_ARRAY = [10, 20, 30, 40]


def twoSumMerge(ar1: List[int], ar2: List[int], x: int):
    ar1, ar2 = copy.deepcopy(ar1), copy.deepcopy(ar2)
    merged = []
    while ar1 and ar2:
        if ar1[0] < ar2[0]:
            merged.append((1, ar1.pop(0)))
        else:
            merged.append((2, ar2.pop(0)))
    merged += [(1, x) for x in ar1] + [(2, x) for x in ar2]

    l, r = 0, len(merged)-1
    diff = inf
    output = (0, 0)
    while l != r:
        curr_sum = merged[l][1] + merged[r][1]
        if (
            merged[l][0] != merged[r][0] and
            abs(curr_sum - x) < diff
        ):
            diff = abs(curr_sum - x)
            output = (merged[l][1], merged[r][1])
        if curr_sum > x:
            r -= 1
        else:
            l += 1

    return output


def twoSumUnmerged(ar1: List[int], ar2: List[int], x: int):
    m,n = len(ar1), len(ar2)
    l, r = 0, n-1
    diff = inf
    output = (0, 0)
    while l < m and r > 0:
        y = ar1[l] + ar2[r]
        if abs(y-x) < diff:
            diff = abs(y-x)
            output = (ar1[l], ar2[r])
        if y > x:
            r -= 1
        else:
            l += 1

    return output

print(FIRST_ARRAY)

print(twoSumMerge(FIRST_ARRAY, SECOND_ARRAY, 37))
print(twoSumUnmerged(FIRST_ARRAY, SECOND_ARRAY, 37))

print(twoSumMerge(FIRST_ARRAY, SECOND_ARRAY, 46))
print(twoSumUnmerged(FIRST_ARRAY, SECOND_ARRAY, 46))
