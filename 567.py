class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False

        s1_freq = dict()
        window_freq = dict()
        for i in range(len(s1)):
            s1_freq[s1[i]] = s1_freq.get(s1[i], 0) + 1
            window_freq[s2[i]] = window_freq.get(s2[i], 0) + 1

        if s1_freq == window_freq:
            return True

        for i in range(len1, len2):
            start_char = s2[i - len1]
            end_char = s2[i]

            window_freq[end_char] = window_freq.get(end_char, 0) + 1
            window_freq[start_char] -= 1

            if not window_freq[start_char]:
                del window_freq[start_char]

            if window_freq == s1_freq:
                return True

        return False 