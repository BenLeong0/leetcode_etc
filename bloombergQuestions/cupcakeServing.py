# Count and remove all groups of size 0 mod k
# 2-sum 3-sum ... n-sum until n > len(arr)

arr = [3,1,1,1,1]




def maxGroups(arr):
    full_length = len(arr)
    k, arr = arr[0], arr[1:]
    arr = [x%k for x in arr]
    arr.sort()
    count = arr.count(0)
    visited = {i for i in range(len(arr)) if arr[i]==0}
    n = 2

    def twoSum(l=0,arr=arr,target=k):
        r = len(arr)-1
        while l<r:
            if l in visited:
                l += 1
                continue
            if r in visited:
                r -= 1
                continue
            s = arr[l]+arr[r]
            if s==target:
                visited.add(l)
                visited.add(r)
                count += 1
                return True
            elif s<target:
                l += 1
            else:
                r += 1
        return False


    def nSum(n=2,l=0,arr=arr,target=k):
        if n==3:
            if twoSum(l=l+1,arr=arr,target=target-arr[l]):
                visited.add(l)
                return True
        else:
            newTarget = target-arr[l]
            for i in range(l+1,len(arr)):
                if i not in visited:
                    if nSum(n=n-1,l=i,target=newTarget):
                        visited.add(l)
                        return True
        return False


    while n <= full_length - len(visited):
        for i in range(full_length-n+1):
            if i not in visited:
                nSum(n=n,l=i)
        n+=1

    if len(visited) < full_length:
        return count+1
    return count

print(maxGroups(arr))
