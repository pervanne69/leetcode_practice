from collections import deque


def numSquares(n: int) -> int:
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1

    queue = deque([n])
    visited = {n}
    level = 0

    while queue:
        level += 1
        for _ in range(len(queue)):
            current = queue.popleft()
            for square in squares:
                next_val = current - square
                if next_val == 0:
                    return level
                if next_val > 0 and next_val not in visited:
                    visited.add(next_val)
                    queue.append(next_val)


print(numSquares(12))