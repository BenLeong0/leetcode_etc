s = '()[]{}'

parentheses = {
    '(': ')',
    '[': ']',
    '{': '}'
}

def f(s=s):
    i = 0
    while s:
        if i >= len(s):
            return False
        elif s[i] in parentheses.keys():
            i += 1
        elif i < 1:
            return False
        elif s[i] == parentheses[s[i-1]]:
            s = s[:i-1] + s[i+1:]
            i -= 1
        else:
            return False
    return True

print(f())
