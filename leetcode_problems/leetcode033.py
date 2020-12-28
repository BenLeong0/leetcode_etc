def f(nums, target):
    l = 0
    r = len(nums)

    if nums[0] == target:
        return 0
    if r == 1:
        return -1

    while r-l > 1:
        if nums[(l+r)//2] > nums[l]:
            l = (l+r)//2
        else:
            r = (l+r)//2
    piv = r
    nums = nums[piv:] + nums[:piv]

    l = 0
    r = len(nums)
    while True:
        print(l,r,(l+r)//2)
        if nums[(l+r)//2] == target:
            x = (l+r)//2
            break
        elif r - l == 1:
            return -1
        elif nums[(l+r)//2] > target:
            r = (l+r)//2
        else:
            l = (l+r)//2

    return (x + piv) % len(nums)

nums = [3,5,1]
target = 5

print(f(nums, target))
