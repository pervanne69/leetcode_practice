# Задача: RLE
# 1 Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBB
# | Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B10



# алгоритм
# заводим счетчик, отвечающий за текущее кол-во текущего символа в слове
# пробегаемся по слову, обновляя счетчик, если буква повторилась
# если же буква другая, то два случая
# счетчик = 1, добавляем букву в результат
# счетчик != 1, добавляем букву + значение счетчика
# обновляем текущую букву и идем дальше до конца
def solution(a: str) -> str:
    if not a:
        return ""
    if len(a) == 1:
        return a

    count = 1
    cur_char = a[0]
    result = ""
    for i in range(1, len(a)):
        if a[i] == cur_char:
            count += 1
        else:
            if count == 1:
                result += cur_char
            else:
                result += f"{cur_char}{count}"
            cur_char = a[i]
            count = 1
        if i == len(a) - 1:
            if count == 1:
                result += cur_char
            else:
                result += f"{cur_char}{count}"
    return result


print(solution("AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBB"))
