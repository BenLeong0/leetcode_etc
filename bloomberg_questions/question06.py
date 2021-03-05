s = "(a(b(c)d)"


def f(s=s):
    s = list(s)
    stack = []
    i = 0
    for (i,char) in enumerate(s):
        if char == ')':
            if not stack:
                s[i] = ''
                continue
            else:
                stack.pop()
        elif char == '(':
            stack.append(i)

    while stack:
        s[stack.pop()] = ''
    return ''.join(s)

print(f())
