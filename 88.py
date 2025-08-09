from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1 = m - 1           # последний элемент nums1, который должен быть учтён
    p2 = n - 1           # последний элемент nums2
    p = m + n - 1        # последний индекс в nums1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # если остались элементы в nums2 — скопировать их (nums1 уже на месте)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


merge(nums1 = [0], m = 0, nums2 = [1], n = 1)