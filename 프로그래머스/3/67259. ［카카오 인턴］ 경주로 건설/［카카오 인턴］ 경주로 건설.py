from collections import deque


def solution(board):
    answer = 0

    # (0, 1) => 위아래, (2, 3) => 좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited = [
        [[int(1e9) for _ in range(2)] for _ in range(len(board[0]))]
        for _ in range(len(board))
    ]
    visited[0][0][0], visited[0][0][1] = 0, 0

    def bfs():
        queue = deque([])
        queue.append((0, 0, 0))  # 위아래
        queue.append((0, 0, 1))  # 좌우

        while queue:
            x, y, direction = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (
                    0 <= nx < len(board)
                    and 0 <= ny < len(board[0])
                    and board[nx][ny] == 0
                ):
                    if direction == 0:
                        if i == 0 or i == 1:
                            if visited[nx][ny][0] >= visited[x][y][0] + 100:
                                visited[nx][ny][0] = visited[x][y][0] + 100
                                queue.append((nx, ny, 0))

                        elif i == 2 or i == 3:
                            if visited[nx][ny][1] >= visited[x][y][0] + 600:
                                visited[nx][ny][1] = visited[x][y][0] + 600
                                queue.append((nx, ny, 1))

                    elif direction == 1:
                        if i == 0 or i == 1:
                            if visited[nx][ny][0] >= visited[x][y][1] + 600:
                                visited[nx][ny][0] = visited[x][y][1] + 600
                                queue.append((nx, ny, 0))

                        elif i == 2 or i == 3:
                            if visited[nx][ny][1] >= visited[x][y][1] + 100:
                                visited[nx][ny][1] = visited[x][y][1] + 100
                                queue.append((nx, ny, 1))
        return

    bfs()

    answer = min(visited[len(board) - 1][len(board[0]) - 1])

    return answer
