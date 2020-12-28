def f(s):
    result = 0
    while s:
        if s[0] == 'M':
            result += 1000

        elif s[0] == 'D':
            result += 500

        elif s[0] == 'C':
            if 'M' in s:
                result += 900
                s = s[1:]
            elif 'D' in s:
                result += 400
                s = s[1:]
            else:
                result += 100

        elif s[0] == 'L':
            result += 50

        elif s[0] == 'X':
            if 'C' in s:
                result += 90
                s = s[1:]
            elif 'L' in s:
                result += 40
                s = s[1:]
            else:
                result += 10

        elif s[0] == 'V':
            result += 5

        else:
            print('yo')
            if 'X' in s:
                result += 9
                s = s[1:]
            elif 'V' in s:
                result += 4
                s = s[1:]
            else:
                result += 1

        s = s[1:]

    return result

print(f('IX'))
