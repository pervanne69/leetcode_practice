def removeStars(s: str) -> str:
    string = [i for i in s]
    star_index = -1
    count = 0
    for i in range(len(string)):
        if string[i] == "*":
            if star_index == -1:
                star_index = i
            count += 1
            if star_index - count >= 0:
                if string[star_index - count] == "":
                    current_index = star_index - count - 1
                    while string[current_index] == "":
                        current_index -= 1
                    string[current_index] = ""
                else:
                    string[star_index - count] = ""
            string[star_index + count - 1] = ""
        else:
            if star_index != -1:
                star_index = -1
                count = 0
    return "".join(string)

print(removeStars("abb*cdfg*****x*"))