
def convert(s: str, numRows: int):
    j = 0
    i = 0
    count = 0
    n = len(s)
    matrix = [["" for _ in range(n)] for __ in range(numRows)]
    while count != n:
        if i < numRows:
            matrix[i][j] = s[count]
            i += 1
            count += 1
        else:
            i = numRows - 2
            if numRows == 1:
                i += 1
            j += 1
            while i != 0 and count != n:
                matrix[i][j] = s[count]
                i -= 1
                j += 1
                count += 1
    result = ""
    for i in range(numRows):
        for j in range(n):
            if matrix[i][j] != "":
                result += matrix[i][j]
    return result


def convert2(s: str, numRows: int):
    j = 0
    i = 0
    count = 0
    n = len(s)
    matrix = [["" for _ in range(n)] for __ in range(numRows)]
    while count != n:
        if i < numRows:
            matrix[i][j] = s[count]
            i += 1
            count += 1
        else:
            i = numRows - 2
            if numRows == 1:
                i += 1
            j += 1
            while i != 0 and count != n:
                matrix[i][j] = s[count]
                i -= 1
                j += 1
                count += 1
    result = ""
    for i in matrix:
        result += ''.join(i)
    return result

def convert2(s: str, numRows: int):
    j = 0
    i = 0
    count = 0
    n = len(s)
    matrix = [["" for _ in range(n)] for __ in range(numRows)]
    while count != n:
        if i < numRows:
            matrix[i][j] = s[count]
            i += 1
            count += 1
        else:
            i = numRows - 2
            if numRows == 1:
                i += 1
            j += 1
            while i != 0 and count != n:
                matrix[i][j] = s[count]
                i -= 1
                j += 1
                count += 1
    result = ""
    for i in matrix:
        result += ''.join(i)
    return result

print(convert2(s = "PAYPALISHIRING", numRows = 4) == "PINALSIGYAHRPI")
print(convert2(s = "PAYPALISHIRING", numRows = 3) == "PAHNAPLSIIGYIR")
print(convert2(s = "AB", numRows = 1) == "AB")
print(convert2(s="ABCDE", numRows = 4))