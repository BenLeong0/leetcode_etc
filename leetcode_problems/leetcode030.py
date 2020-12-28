def f(s,words):
    wordLength = len(words[0])
    substringLength = wordLength * len(words)
    sols = []

    for i in range(len(s) - substringLength + 1):
        word = s[i:i+wordLength]
        if word in words:
            newWords = words[:]
            newWords.remove(word)
            if g(s[i+wordLength:], newWords, wordLength):
                sols.append(i)

    return sols


def g(s,words,wordLength):
    if len(words) == 0:
        return True
    word = s[:wordLength]
    if word in words:
        newWords = words[:]
        newWords.remove(word)
        return g(s[wordLength:], newWords, wordLength)
    return False

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

print(f(s,words))
