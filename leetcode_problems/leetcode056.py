# Two 'pointer'

def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    currStart, currEnd = intervals[0]
    output = []
    for start, end in intervals[1:]:
        if start > currEnd:
            output.append([currStart, currEnd])
            currStart, currEnd = start, end
        elif end > currEnd:
            currEnd = end
    output.append([currStart, currEnd])

    return output


intervals = [[1,3],[2,6],[8,10],[15,18]]

print(merge(intervals))
