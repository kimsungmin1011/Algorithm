from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    queue = deque([(a, b)])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and graph[nx][ny] == "L"
                and visited[nx][ny] == -1
            ):
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    max_value = -1
    for i in visited:
        max_value = max(max_value, max(i))

    return max_value


answer = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            answer = max(answer, bfs(i, j))

print(answer)
