def mergesort(arr):
    if len(arr)<=1:
        return arr

    A = arr[:len(arr)//2]
    B = arr[len(arr)//2:]
    return merge(mergesort(A),mergesort(B))


def merge(A,B):
    l=r=0
    output = []
    while l<len(A) and r<len(B):
        if A[l] < B[r]:
            output.append(A[l])
            l += 1
        else:
            output.append(B[r])
            r += 1
    return output + A[l:] + B[r:]


arr = [7,6,4,95,3,1,64,2,5,5,4,6,7,5,13,5,4,896,876,1,351,34,874,8,6,6,4,6,53,7,37,34,]

print(mergesort(arr))
