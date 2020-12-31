def f(arr):
    for i in range(len(arr)):
        if arr[i] != -1 and arr[i] != i:
            x = arr[i]
            while arr[x] != x and arr[x] != -1:
                y = arr[x]
                arr[x] = x
                x = y
            arr[x] = x
            if arr[i] != i:
                arr[i] = -1


arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
f(arr)
null = None

a = [9,5,4,5,null,2,6,2,5,null,8,3,9,2,3,1,1,null,4,5,4,2,2,6,4,null,null,1,7,null,5,4,7,null,null,7,null,1,5,6,1,null,null,null,null,9,2,null,9,7,2,1,null,null,null,6,null,null,null,null,null,null,null,null,null,5,null,null,3,null,null,null,8,null,1,null,null,8,null,null,null,null,2,null,8,7]
print(a[0:1], 1-0, 1-0-a[0:1].count(None))
print(a[1:3], 3-1, 3-1-a[1:3].count(None))
print(a[3:7], 7-3, 7-3-a[3:7].count(None))
print(a[7:13], 13-7, 13-7-a[7:13].count(null))
print(a[13:23], 23-13, 23-13-a[13:23].count(null))
print(a[23:41], 41-23, 41-23-a[23:41].count(null))
print(a[41:65], 65-41, 65-41-a[41:65].count(null))
print(a[65:79], 79-65, 79-65-a[65:79].count(null))
print(a[79:89], 89-79, 89-79-a[79:89].count(null))
