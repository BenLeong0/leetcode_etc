binString = '1111000110010110100110101001011000'


def largestGood(binString=binString):

    def rec_sort(binString=binString):
        if len(binString) == 0:
            return ''
        currCount = 0
        currStart = 0
        substrings = []

        for i in range(len(binString)):
            if binString[i] == '1':
                currCount += 1
            else:
                currCount -= 1
                if currCount == 0:
                    res = rec_sort(binString[currStart+1:i])
                    substrings.append('1' + res + '0')
                    currStart = i+1
        ## Submitted method (wrong)
        # max_length = len(max(substrings, key=len))
        # print(substrings)
        # substrings.sort(key=lambda x: int(x.ljust(max_length, '0'),2), reverse=True)
        substrings.sort(reverse=True)
        return ''.join(substrings)
    return rec_sort()


print(largestGood())
