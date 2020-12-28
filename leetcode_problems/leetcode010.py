s = "b"
p = "c"


def arrange(p):
    #  CHANGE: go from back to front (eg 'a*a*a')
    for (i,x) in enumerate(p[:-2]):
        if p[i+1] == '*' and p[i+2] == x:
            if i+3 < len(p):
                if p[i+3] == '*':
                    continue
            p = p[:i+1] + p[i] + '*' + p[i+3:]
    return p

# p = arrange(p)



def f(s=s,p=p):
    if not s:
        if 2*p.count('*') == len(p):
            return True
        return False
    if not p:
        return False

    if len(p) == 1:
        if len(s) > 1:
            return False
        elif p == '.' or p == s:
            return True
        return False

    if p[1] == '*':
        poss = [s]
        i = 0
        while s[i] == p[0] or p[0] == '.':
            poss.append(s[i+1:])
            i += 1
            if i == len(s): break
        print(poss)
        for newS in poss:
            if f(newS, p[2:]):
                return True
        return False

    elif p[0] == '.' or p[0] == s[0]:
        return f(s[1:], p[1:])

    return False


print(f())
