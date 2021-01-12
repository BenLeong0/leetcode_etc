"""
Longest substring without repeating characters

>> two pointer
"""

def longestSubstring(s):
    i = j = 0
    maxLength = 0
    max_i = max_j = 0
    while j!=len(s):
        if s[j] not in s[i:j]:
            j += 1
            if j-i>maxLength:
                maxLength = j - i
                max_i, max_j = i, j
        else:
            i += 1
    return s[max_i:max_j]

print(longestSubstring('pwwkew'))
