def findMaxLength(nums):
    # Словарь, где ключ — сумма, а значение — индекс, где эта сумма встретилась впервые
    first_index_by_sum = {0: -1}

    current_sum = 0
    max_length = 0

    for index in range(len(nums)):
        if nums[index] == 0:
            current_sum -= 1
        else:
            current_sum += 1

        if current_sum in first_index_by_sum:
            previous_index = first_index_by_sum[current_sum]
            length = index - previous_index
            max_length = max(max_length, length)
        else:
            first_index_by_sum[current_sum] = index
    return max_length


print(findMaxLength(nums = [0,1,1,1,1,1,0,0,0]))