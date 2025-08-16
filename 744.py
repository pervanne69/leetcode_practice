from typing import List


def nextGreatestLetter(letters: List[str], target: str) -> str:
    def less_than_char(char1, char2):
        return ord(char1) <= ord(char2)

    left = 0
    right = len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if less_than_char(letters[mid], target):
            left = mid + 1
        else:
            right = mid - 1
    return letters[left % len(letters)]


print(nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))