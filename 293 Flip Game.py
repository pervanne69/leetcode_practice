# Description
# You are playing the following Flip Game with your friend: Given a string
# that contains only two characters: + and -, you can flip two consecutive "++" into "--",
# you can only flip one time. Please find all strings that can be obtained after one flip.
#
# Write a program to find all possible states of the string after one valid move.
# Example
# Example1
#
# Input:  s = "++++"
# Output:
# [
#   "--++",
#   "+--+",
#   "++--"
# ]
# Example2
#
# Input: s = "---+++-+++-+"
# Output:
# [
# 	"---+++-+---+",
# 	"---+++---+-+",
# 	"---+---+++-+",
# 	"-----+-+++-+"
# ]
from typing import List


def generate_possible_next_moves(s: str) -> List[str]:
    result = []
    left = 0
    for right in range(1, len(s)):
        if s[left] == "+" and s[right] == "+":
            result.append(s[:left] + "--" + s[right + 1:])
        left += 1
    return result


print(generate_possible_next_moves("---+++-+++-+"))