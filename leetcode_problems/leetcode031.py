def f(nums):
    nums[:] = nums[::-1]
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            if i == 0:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                nums[:] = nums[::-1]
            else:
                j = i
                while nums[j-1] > nums[i+1]:
                    j -= 1
                    if j == 0:
                        break
                nums[j], nums[i+1] = nums[i+1], nums[j]
                print(nums,i,nums[i:-1:-1])
                nums[:i+1] = nums[i::-1]
                nums[:] = nums[::-1]
            break
    print(nums)





nums = [1,3,2]
print(f(nums))
