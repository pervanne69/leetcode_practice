def is_strobogrammatic(num: str) -> bool:
    strobo_nums = {"6": "9", "9": "6", "8": "8", "1": "1", "0": "0"}
    result = ""
    for char in num:
        if char not in strobo_nums or strobo_nums[strobo_nums[char]] != char:
            return False
        result += strobo_nums[char]
    return result[-1::-1] == num