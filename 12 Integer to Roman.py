def intToRoman(num: int) -> str:
    values = [1000, 500, 100, 50, 10, 5, 1]
    symbols = ["M", "D", "C", "L", "X", "V", "I"]
    v_s = {values[i]: symbols[i] for i in range(len(values))}
    index = 0
    div_el = 1000
    result = ""
    while num != 0:
        if num >= values[index]:
            first_digit = num // div_el
            if first_digit in [4, 9]:
                if first_digit == 9:
                    result += v_s[values[index + 1]] + v_s[values[index - 1]]
                    num -= (values[index - 1] - values[index + 1])
                else:
                    result += v_s[values[index]] + v_s[values[index - 1]]
                    num -= (values[index - 1] - values[index])
            else:
                result += v_s[values[index]]
                num -= values[index]
        else:
            index += 1
            if index == 0:
                div_el = 1000
            elif 1 <= index <= 2:
                div_el = 100
            elif 3 <= index <= 4:
                div_el = 10
            else:
                div_el = 1
    return result


print(intToRoman(1994))



