from random import choice
print(choice([1, 2, 3, 4]))


class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """

    def is_one_edit_distance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        if len(t) == len(s):
            count = 0
            for i in range(len(t)):
                if t[i] != s[i]:
                    count += 1
                if count > 1:
                    return False
            return count == 1

        else:
            len_s, len_t = len(s), len(t)
            if len(t) > len(s):
                s, t, = t, s
                len_s, len_t = len_t, len_s
            i = j = 0
            count = 0
            while i < len_s and j < len_t:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    count += 1
                    i += 1
                    if count > 1:
                        return False
            return True
