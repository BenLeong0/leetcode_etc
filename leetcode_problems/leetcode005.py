def longestPalindromeDP(s):
    n = len(s)
    P = [[False]*n for i in range(n)]
    ans = ''
    maxLength = 0
    for j in range(n):
        for i in range(j+1):
            print(i,j)
            if j == i:
                P[i][j] = True
            elif j == i+1 and s[i] == s[j]:
                P[i][j] = True
            elif (s[i] == s[j]) and (P[i+1][j-1]):
                P[i][j] = True
            else:
                continue

            if j - i + 1 > maxLength:
                ans = s[i:j+1]
                maxLength = j - i + 1

    print(ans)
    return ans


def longestPalindromeCentres(s):
    n = len(s)
    if n <= 1:
        return s

    def expandAroundCentre(l,r,maxLength,ans):
        while l>=0 and r<n and s[l]==s[r]:
            l -= 1
            r += 1
        if r - l - 1 > maxLength:
            return r-l-1, s[l+1:r]
        return maxLength, ans

    ans = ''
    maxLength = 0
    for i in range(n-1):
        maxLength, ans = expandAroundCentre(i,i,maxLength,ans)
        maxLength, ans = expandAroundCentre(i,i+1,maxLength,ans)

    print(ans)
    return ans






s = 'cbbd'
longestPalindromeCentres(s)
