from typing import List


def valid_word_square(words: List[str]) -> bool:
    max_len = len(max(words, key=lambda x: len(x)))
    for i in range(len(words)):
        words[i] = words[i].ljust(max_len, " ")
    words_tmp = "".join(words)
    d = {}
    for i in range(len(words_tmp)):
        if i % max_len in d:
            d[i % max_len] += words_tmp[i]
        else:
            d[i % max_len] = words_tmp[i]
    for i in d:
        if d[i] != words[i]:
            return False
    return True


def sol2(words: List[str]) -> bool:
    n = len(words)
    for i in range(n):
        if len(words[i]) > n:
            return False
        column = []
        for word in words:
            if i < len(word):
                column.append(word[i])
            else:
                pass
        if ''.join(column) != words[i]:
            return False
    return True

def sol3(words: List[str]) -> bool:
    if not words:
        return True
    max_len = max(len(word) for word in words)
    n = len(words)
    if max_len > n:
        return False
    words_padded = [word.ljust(n) for word in words]
    for i in range(n):
        column = []
        for word in words_padded:
            if i < len(word):
                column.append(word[i])
            else:
                column.append(' ')
        if ''.join(column).rstrip() != words[i].rstrip():
            return False
    return True

print(valid_word_square([
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]


))
