from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    counts1 = dict()
    result = []
    for i in nums1:
        counts1[i] = counts1.get(i, 0) + 1

    for num in nums2:
        if counts1.get(num, 0) > 0:
            result.append(num)
            counts1[num] -= 1

    return result