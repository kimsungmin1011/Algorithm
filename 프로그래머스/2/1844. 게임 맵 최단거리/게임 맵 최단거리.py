from collections import deque


def solution(maps):
    answer = 0
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    n = len(maps)
    m = len(maps[0])
    visited = [[-1 for _ in range(m)] for _ in range(n)]

    def bfs():
        queue = deque([(0, 0)])
        visited[0][0] = 1
        while queue:
            x, y = queue.popleft()
            if x == n - 1 and y == m - 1:
                return visited[n - 1][m - 1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1 and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
        return -1

    answer = bfs()

    return answer