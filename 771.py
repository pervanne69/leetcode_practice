def numJewelsInStones(jewels: str, stones: str) -> int:
    result = 0
    j_freq = dict()
    for i in jewels:
        j_freq[i] = j_freq.get(i, 0) + 1
    for i in stones:
        if i in j_freq:
            result += 1
    return result
