def isMatch(s: str, p: str) -> bool:
    p_index = s_index = 0
    n = len(s)
    m = len(p)
    while p_index < m and s_index < n:
        cur_char = p[p_index]
        if cur_char == s[s_index]:
            s_index += 1
        elif cur_char == ".":
            s_index += 1
        elif cur_char == "*":
            s_cur_char = s[s_index]
            while s_index < n and s[s_index] == s_cur_char:
                s_index += 1
        p_index += 1
    if s_index != n:
        return False
    if s_index == n and p_index != m:
        
        if p[p_index] == p[s_index] and s_index - 1 == p_index:
            return True
        return False
    return True


print(isMatch(s = "aaa", p = "aaaa"))