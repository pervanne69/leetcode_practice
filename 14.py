def run1(strs) -> str:
    items = list(sorted(strs, key=lambda x: len(x)))
    first = items[0]
    common = ""
    for i in range(len(first)):
        current = first[0:i + 1]
        for j in range(len(items)):
            if len(items[j]) >= i + 1:
                if items[j][0:i + 1] != current:
                    break
            else:
                break
        else:
            common = current

    return common

a = ["flower","flow","flight"]
print(run1(a))
print(list(sorted(a, key=lambda x: len(x))))