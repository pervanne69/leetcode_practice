# def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
#     def maxConsecutive(target: str) -> int:
#         left = 0
#         changes = 0
#         max_len = 0
#
#         for right in range(len(answerKey)):
#             if answerKey[right] != target:
#                 changes += 1
#
#             while changes > k:
#                 if answerKey[left] != target:
#                     changes -= 1
#                 left += 1
#
#             max_len = max(max_len, right - left + 1)
#         return max_len
#
#     return max(maxConsecutive('T'), maxConsecutive('F'))
#
#
#
# print(maxConsecutiveAnswers(answerKey = "TFFT", k = 1))