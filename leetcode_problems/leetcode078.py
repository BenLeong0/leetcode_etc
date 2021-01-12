"""
Return power set of nums

Dynamic programming!
"""

def subsets(nums):
    curr = [[]]
    for n in nums:
        curr += [x+[n] for x in curr]
    return curr

nums = [1,2,3]
print(subsets(nums))
