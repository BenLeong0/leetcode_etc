def decodeString(s):
    def push(e, arr, depth):
        while depth:
            arr = arr[-1]
            depth -= 1
        arr.append(e)

    def deepPop(arr, depth):
        while depth:
            arr = arr[-1]
            depth -= 1
        return arr.pop()

    s = list(s)
    result = []
    depth = 0
    currInt = 0

    for char in s:
        try:
            currInt = 10*currInt + int(char)
        except:
            if char == '[':
                push(currInt,result,depth)
                push([],result,depth)
                currInt = 0
                depth += 1
            elif char == ']':
                depth -= 1
                subString = ''.join(deepPop(result, depth))
                factor = deepPop(result,depth)
                push(factor*subString,result,depth)
            else:
                push(char,result,depth)

    return ''.join(result)

s = "3[a]2[bc]"
print(decodeString(s))
