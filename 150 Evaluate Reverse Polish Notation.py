# from typing import List
#
#
# def evalRPN(tokens: List[str]) -> int:
#     stack = []
#     n = len(tokens)
#     tokens = list(map(lambda x: int(x) if x.isdigit() or x[1:].isdigit() else x, tokens))
#     if n == 1:
#         return int(tokens[0])
#     for i in range(n):
#         if isinstance(tokens[i], int):
#             stack.append(tokens[i])
#         else:
#             operation = tokens[i]
#             a = stack.pop()
#             b = stack.pop()
#             match operation:
#                 case "+":
#                     stack.append(b + a)
#                 case "-":
#                     stack.append(b - a)
#                 case "*":
#                     stack.append(b * a)
#                 case "/":
#                     stack.append(int(float(b) / a))
#     return stack[0]
#
#
# # print(evalRPN(tokens = ["2","1","+","3","*"]))
# # print(evalRPN(tokens = ["4","13","5","/","+"]))
#
# print(evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

print(len(str(26 ** 120)))