from typing import List


def findRadius(houses: List[int], heaters: List[int]) -> int:
    mini = 0
    houses.sort()
    heaters.sort()
    for house in houses:
        radius = find_closest_heater(heaters, house)
        mini = max(mini, radius)
    return mini


def find_closest_heater(heaters: List[int], house: int) -> int:
    left = 0
    right = len(heaters) - 1
    while left <= right:
        mid = (left + right) // 2
        if heaters[mid] == house:
            return 0
        elif heaters[mid] > house:
            right = mid - 1
        elif heaters[mid] < house:
            left = mid + 1

    candidates = []
    if left < len(heaters):
        candidates.append(abs(heaters[left] - house))
    if left > 0:
        candidates.append(abs(house - heaters[left - 1]))
    return min(candidates) if candidates else 0






# print(findRadius(houses = [1,2,3], heaters = [2]))
# print(findRadius(houses = [1,2,3,4], heaters = [2, 4, 5, 6, 7, 8, 9]))
print(findRadius(houses = [1,5], heaters = [2]))