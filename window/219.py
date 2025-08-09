from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    idxs = dict()
    for i in range(len(nums)):
        if nums[i] in idxs:
            previous_idx = idxs[nums[i]]
            diff = i - previous_idx
            if diff <= k:
                return True
        idxs[nums[i]] = i
    return False


print(containsNearbyDuplicate(nums = [1,0,1,1], k = 1))