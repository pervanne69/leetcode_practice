from typing import List

def groupAnagrams(strs: List[str]):
    d = {}
    for i in strs:
        key = tuple(sorted(i))
        if key not in d:
            d[key] = []
        d[key].append(i)
    return list(d.values())




print(groupAnagrams(strs = ["a"]))