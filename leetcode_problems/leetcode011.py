height = [1,8,6,2,5,4,8,3,7]

l = 0
r = len(height) - 1
maxArea = 0

while l != r:
    maxArea = max(maxArea,(r-l) * min(height[l], height[r]))
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1


print(maxArea)
