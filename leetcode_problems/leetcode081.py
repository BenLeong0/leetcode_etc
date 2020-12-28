def f(nums, target):
    l = 0
    r = len(nums)

    if not nums:
    	return False

    while r-l > 1:
        if nums[(l+r)//2] >= nums[l]:
            l = (l+r)//2
        else:
            r = (l+r)//2
    piv = r
    print(piv)
    nums = nums[piv:] + nums[:piv]

    l = 0
    r = len(nums)
    while True:
        print(nums,l,r)
        if nums[(l+r)//2] == target:
            return True
        elif r - l == 1:
            return False
        elif nums[(l+r)//2] >= target:
            r = (l+r)//2
        else:
            l = (l+r)//2

nums = [1,3,1,1]
target = 3

print(f(nums, target))
