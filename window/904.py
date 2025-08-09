from typing import List


def totalFruit(fruits: List[int]) -> int:

    count = dict()
    left = 0
    max_length = 0

    for right in range(len(fruits)):
        count[fruits[right]] = count.get(fruits[right], 0) + 1

        while len(count) > 2:
            count[fruits[left]] = count.get(fruits[left], 0) - 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


print(totalFruit(fruits = [0,1,2,2]))