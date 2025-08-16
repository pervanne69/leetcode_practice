from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums2.sort()
    result = set()
    for num in nums1:
        left = 0
        right = len(nums2) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums2[mid] == num:
                result.add(num)
                break
            elif nums2[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
    return list(result)



print(intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))