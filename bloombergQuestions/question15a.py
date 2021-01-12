"""
Insert spaces into the string to form series of valid words (in wordDict).
> uses backtracking and memoisation !!
"""


def wordBreak(s, wordDict):
    cache = {'':['']}
    def checkRem(s):
        if s in cache:
            return cache[s]

        results = []
        for word in wordDict:
            if s[:len(word)] == word:
                if s[len(word):]:
                    results += [word + ' ' + x for x in checkRem(s[len(word):])]
                else:
                    results.append(word)
        cache[s] = results
        return results

    return [x for x in checkRem(s)]

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

print(wordBreak(s,wordDict))
