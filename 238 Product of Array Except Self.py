from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    pass


def sol1(nums: List[int]) -> List[int]:
    n = len(nums)
    products = [0 for i in range(n)]
    result = 1
    zero_counter = nums.count(0)
    if zero_counter >= 2:
        return products
    for i in range(n):
        if nums[i] != 0:
            result *= nums[i]
    for i in range(n):
        if nums[i] == 0:
            products[i] = result
        else:
            if zero_counter == 1:
                products[i] = 0
            else:
                products[i] = result // nums[i]
    return products


def sol2(nums: List[int]):
    n = len(nums)
    answer = [1] * n

    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]


print(sol2([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
print(productExceptSelf([0, 0, 0, 0, 0]))
print(productExceptSelf([-1, 1, -1, 1, -1]))
print(productExceptSelf([2, -2]))