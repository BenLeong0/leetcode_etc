def mergesort(arr):
    if len(arr) <= 1:
        return arr

    first_half = arr[:len(arr)//2]
    second_half = arr[len(arr)//2:]
    return merge(mergesort(first_half), mergesort(second_half))


def merge(arr1,arr2):
    l=r=0
    output = []
    while l < len(arr1) and r < len(arr2):
        if arr1[l] < arr2[r]:
            output.append(arr1[l])
            l += 1
        else:
            output.append(arr2[r])
            r += 1
    return output + arr1[l:] + arr2[r:]


arr = [7,6,4,95,3,1,64,2,5,5,4,6,7,5,13,5,4,896,876,1,351,34,874,8,6,6,4,6,53,7,37,34]

print(mergesort(arr))
