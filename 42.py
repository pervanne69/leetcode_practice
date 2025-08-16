# Идея алгоритма. Мы пробегаемся слева направо по массиву высот
# На каждой итерации у нас меняется состояние максимальной высоты
# если нам попалась высота, которая меньше максимума, то мы прибавляем
# к нашему счетчику разницу между максимальной высотой и текущей
# если же мы встретили высоту, которая больше максимальной, то мы обновляем максимум
from typing import List


def sol2(height: List[int]) -> int:
    total = 0
    current_maximum = 0
    absolute_maximum = max(height)
    maximum_index = 0
    for i in range(height.index(absolute_maximum) + 1):
        if height[i] > current_maximum:
            current_maximum = height[i]
            maximum_index = i
        else:
            total += current_maximum - height[i]

    current_maximum = 0
    for i in range(len(height) - 1, maximum_index - 1, -1):
        if height[i] > current_maximum:
            current_maximum = height[i]
        else:
            total += current_maximum - height[i]

    return total


print(sol2(height = [0,1,0,2,1,0,1,3,2,1,2,1]))