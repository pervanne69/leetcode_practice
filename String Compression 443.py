class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        if len(chars) == 1:
            s = chars[0]
        else:
            letter = chars[0]
            count = 1
            for i in range(1, len(chars)):
                if letter == chars[i]:
                    count += 1
                else:
                    if count != 1:
                        s += f"{letter}{count}"
                    else:
                        s += letter
                    letter = chars[i]
                    count = 1
            if count != 1:
                s += f"{letter}{count}"
            else:
                s += letter
        for i in range(len(s)):
            chars[i] = list(s)[i]
        return len(chars[:len(s)])
