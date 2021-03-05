array = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76]
ranges = [[5, 8], [10, 13], [3, 6], [20, 25]]


def removeRanges_sort():
    ranges.sort(key=lambda x:x[0])
    i = 0
    while i < len(ranges)-1:
        if ranges[i][1] > ranges[i+1][1]:
            del ranges[i+1]
        elif ranges[i][1] > ranges[i+1][0]:
            ranges[i][1] = ranges[i+1][1]
            del ranges[i+1]
        else:
            i+=1
    ranges.append([len(array)]*2)

    output = []
    rangeId = 0
    for (i,el) in enumerate(array):
        if ranges[rangeId][0] <= i < ranges[rangeId][1]:
            continue
        if i == ranges[rangeId][1]:
            rangeId += 1
        output.append(el)
    return output


def removeRanges_markers():
    checks = [0] * max(ranges,key=lambda x:x[1])+1
    for start, end in ranges:
        checks[start] = 1
        if checks[end] == 0:
            checks[end] = -1


    output = []




print(removeRanges_sort())
