def findMedianSortedArrays(nums1, nums2) -> float:
    mergedArray = []
    while nums1 and nums2:
        if nums1[0] < nums2[0]:
            mergedArray.append(nums1.pop(0))
        else:
            mergedArray.append(nums2.pop(0))
    mergedArray += nums1 + nums2

    fullLength = len(mergedArray)
    if fullLength % 2 == 0:
        return (mergedArray[fullLength//2] + mergedArray[fullLength//2 - 1]) / 2
    else:
        return float(mergedArray[fullLength//2])


print(findMedianSortedArrays([1,3], [2]))
