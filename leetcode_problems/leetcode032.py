def f(s):
    stack = [-1]
    currMax = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) > 1:
                stack.pop()
                currMax = max(currMax, i - stack[-1])
            else:
                stack = [i]
    return currMax

s = ")()())"
print(f(s))

'(())()(()'
