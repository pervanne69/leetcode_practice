def findTheDifference(s: str, t: str) -> str:
    s_list = [0] * 26
    t_list = [0] * 26
    result_index = 0
    for i in s:
        s_list[ord(i) - ord("a")] += 1
    for i in t:
        t_list[ord(i) - ord("a")] += 1
    for i in range(26):
        if s_list[i] ^ t_list[i] != 0:
            result_index = i
            break
    return chr(result_index + ord("a"))


def sol2(s: str, t: str) -> str:
    res = 0
    for c in s + t:
        res ^= ord(c)
    return chr(res)


print(findTheDifference(s = "", t = "y"))