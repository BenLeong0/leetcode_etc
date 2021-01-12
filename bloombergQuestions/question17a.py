def firstUniqueElementSlow(arr):
    visited = set()
    stack = []
    def check(i):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return False
        return True

    for i in range(len(arr)):
        if check(i):
            return arr[i]

def firstUniqueElementBig(arr):
    visited = {}
    for (i,x) in enumerate(arr):
        if x in visited:
            visited[x] = -1
        else:
            visited[x] = i

    filtered = [x for x in list(visited.items()) if x[1] != -1]
    return min(filtered, key=lambda x:x[1])[0]


arr = [1,2,3,4,1,5,4,2]

print(firstUniqueElementSlow(arr))
print(firstUniqueElementBig(arr))
