from typing import List


def longestPalindrome(words: List[str]) -> int:
    count = dict()
    for word in words:
        count[word] = count.get(word, 0) + 1
    result = 0
    center_used = False

    for word, freq in list(count.items()):
        rev = word[::-1]

        if word == rev:
            pairs = freq // 2
            result += pairs * len(word) * 2
            count[word] -= pairs * 2
            if count[word] > 0 and not center_used:
                result += len(word)
                center_used = True
        elif word < rev:  # чтобы не пересчитывать пару дважды
            if rev in count:
                pairs = min(count[word], count[rev])
                result += pairs * len(word) * 2

    return result



print(longestPalindrome(["ab","ty","yt","lc","cl","ab"]))