def compareVersion(version1: str, version2: str) -> int:
    version1 = list(map(int, version1.split('.')))
    version2 = list(map(int, version2.split('.')))
    max_length = max(len(version1), len(version2))
    if len(version1) > len(version2):
        version2 = [i for i in version2] + [0 for _ in range(max_length - len(version2))]
    elif len(version1) < len(version2):
        version1 = [i for i in version1] + [0 for _ in range(max_length - len(version1))]
    first = 0
    while first < max_length:
        digit1, digit2 = version1[first], version2[first]
        if digit1 > digit2:
            return 1
        elif digit1 < digit2:
            return -1
        first += 1
    return 0


# print(compareVersion("1.2.3", "1.2.3"))
# print(compareVersion("1.2", "1.10"))
# print(compareVersion(version1 = "1.01", version2 = "1.001"))
print(compareVersion("1.0", "1.0.0.0"))
