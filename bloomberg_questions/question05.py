from math import inf
s = "aaabbbacd"

def candyCrushRecursion(s=s):
    print(s)
    i = 0
    while i < len(s)-2:
        if s[i] == s[i+1] == s[i+2]:
            return s[:i] + candyCrush(s[i+3:])
        else:
            i += 1
    return s


def candyCrushStack(s=s):
    if not s:
        return ''

    stack = [[s[0], 1]]
    for letter in s[1:]:
        if stack:
            if stack[-1][0] == letter:
                stack[-1][1] += 1
                if stack[-1][1] == 3:
                    stack.pop()
                while len(stack) > 1:
                    if stack[-1][0] == stack[-2][0]:
                        if stack[-1][1] + stack[-2][1] == 3:
                            stack = stack[:-2]
                        else:
                            stack[-2][1] %= stack[-1][1] + stack[-2][1]
                            stack.pop()
                    else:
                        break
            else:
                stack.append([letter,1])
        else:
            stack.append([letter,1])
    result = ''.join([item[0]*item[1] for item in stack])
    return result


def candyCrushOptimal(s=s):
    if not s:
        return ''
    chains = [[s[0],1]]
    for letter in s[1:]:
        if chains[-1][0] == letter:
            chains[-1][1] += 1
        else:
            chains.append([letter,1])

    def f(chains=chains):
        i = 0
        while i < len(chains)-1:
            if chains[i][0] == chains[i+1][0]:
                chains[i][1] += chains[i+1][1]
                del chains[i+1]
            else:
                i += 1

        result = ''
        for (i, chain) in enumerate(chains):
            if chain[1] >= 3:
                if not result:
                    result = f(chains[:i] + chains[i+1:])
                else:
                    result = min(result,f(chains[:i] + chains[i+1:]),key=len)
        if not result:
            return ''.join([x[0]*x[1] for x in chains])
        return result

    return f()




print(candyCrushStack())
print(candyCrushOptimal())
