def printAllSubsets(s):
    subsets = {''}
    for letter in s:
        newSubsets = set()
        for subset in subsets:
            newSubsets.add(subset+letter)
        subsets = subsets.union(newSubsets)

    subsets = list(subsets)
    subsets.sort()
    subsets.sort(key=lambda x: len(x))
    for subset in subsets:
        print(subset)

# printAllSubsets('abc')
printAllSubsets('aabc')
