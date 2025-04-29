from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    line = list(input())
    line = [int(i) for i in line]
    graph.append(line)

visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


bfs()

print(visited[n - 1][m - 1])
