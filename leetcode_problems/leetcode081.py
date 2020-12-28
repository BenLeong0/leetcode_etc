def f(nums, target):
    if not nums:
    	return False

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums = nums[i+1:] + nums[:i+1]
            break

    l = 0
    r = len(nums)
    while True:
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
