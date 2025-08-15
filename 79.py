from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(row, col, index):
        if index == len(word):
            return True
        if row < 0 or col < 0 or row >= rows or col >= cols:
            return False
        if board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = "#"

        found = (
                dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1)
        )

        board[row][col] = temp
        return found

    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0):
                return True
    return False


print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
