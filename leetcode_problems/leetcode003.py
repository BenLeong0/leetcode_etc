def lengthOfLongestSubstring(s):
    i, j = 0, 0
    ans = 0
    while j != len(s):
        if s[j] in s[i:j]:
            i += 1
        else:
            j += 1
        ans = max(ans, j-i)
    return ans

s = "abcabcbb"

print(lengthOfLongestSubstring(s))
