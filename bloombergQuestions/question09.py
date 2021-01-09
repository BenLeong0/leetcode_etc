def isAnagram(s,t):
    if len(s) != len(t):
        return False

    letterCounts = {}

    for char in s:
        if char in letterCounts:
            letterCounts[char] += 1
        else:
            letterCounts[char] = 1

    for char in t:
        if char not in letterCounts:
            return False
        elif letterCounts[char] == 0:
            return False
        letterCounts[char] -= 1

    return True


s = "anagram"
t = "nagaram"

print(validAnagram(s,t))
