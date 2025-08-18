import random


# class RandomizedSet:
#
#     def __init__(self):
#         self.d = {}      # Словарь для хранения значений и их индексов
#         self.values = []  # Список для случайного выбора
#
#     def insert(self, val: int) -> bool:
#         if val in self.d:
#             return False
#         self.d[val] = len(self.values)
#         self.values.append(val)
#         return True
#
#     def remove(self, val: int) -> bool:
#         if val not in self.d:
#             return False
#
#         # Индекс удаляемого элемента
#         idx = self.d[val]
#
#         # Последний элемент в списке
#         last_val = self.values[-1]
#
#         # Перемещаем последний элемент на место удаляемого
#         self.values[idx] = last_val
#         self.d[last_val] = idx
#
#         # Удаляем последний элемент (теперь он дублируется)
#         self.values.pop()
#         del self.d[val]
#
#         return True
#
#     def getRandom(self) -> int:
#         return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.values)
        self.values.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False

        last_val = self.values[-1]
        remove_element_index = self.d[val]

        self.values[remove_element_index] = last_val
        self.d[last_val] = remove_element_index

        self.values.pop()
        del self.d[val]

        return True


    def getRandom(self) -> int:
        return random.choice(self.values)



randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))
print(randomizedSet.remove(2))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())
print(randomizedSet.remove(1))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())