def printAllSubsets(s):
    subsets = {''}
    for letter in s:
        newSubsets = set()
        for subset in subsets:
            newSubsets.add(subset + letter)
        subsets.update(newSubsets)

    sorted_subsets = sorted(subsets, key=lambda x: len(x))
    for subset in sorted_subsets:
        print(subset)

# printAllSubsets('abc')
printAllSubsets('aabc')
