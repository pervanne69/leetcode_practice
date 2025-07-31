def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.find(needle)
    return -1

print(strStr(haystack = "sadbutsad", needle = "sad"))
print(strStr(haystack = "leetcode", needle = "leeto"))