# a->1, b->2, ... , z->26
# 'ab' -> '12', but also 'l' -> '12'!
# Given a number string, how many strings could it have been encoded from?

# DYNAMIC PROGRAMMING : How many up to i'th letter?

def number_of_precodes(s):
    if not s:
        return 1
    s = list(s)
    for char in s:
        if char not in '123456789':
            return 0

    mem_count = [1]
    for (i, char) in enumerate(s):
        if i == 0:
            mem_count.append(1)
        elif int(s[i-1] + s[i]) <= 26:
            mem_count.append(mem_count[-1]+mem_count[-2])
        else:
            mem_count.append(mem_count[-1])

    return mem_count[-1]


def rec_init(s):
    if not s:
        return 1
    s = list(s)
    for char in s:
        if char not in '123456789':
            return 0
    memo = {}
    return number_of_ways(s,0,memo)

def number_of_ways(s,i,memo):
    if i >= len(s)-1:
        return 1
    if i in memo:
        return memo[i]

    result = number_of_ways(s,i+1,memo)
    if int(s[i]+s[i+1])<=26:
        result += number_of_ways(s,i+2,memo)
    memo[i] = result
    return result


print(number_of_precodes('111111211'))
print(rec_init('111111211'))
