arr = [3,1,3,4]

def getMaxValue(arr):
    sorted_arr = sorted(arr)
    sorted_arr[0] = 1
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] > sorted_arr[i-1]:
            sorted_arr[i] = sorted_arr[i-1] + 1

    return sorted_arr[-1]


print(getMaxValue(arr))
