from collections import deque

n = int(input())
graph = []

for i in range(n):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, color):
    queue = deque([(a, b)])
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == color and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


normal_count = 0
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            normal_count += 1
            bfs(i, j, graph[i][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

saekyak_count = 0
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            saekyak_count += 1
            bfs(i, j, graph[i][j])

print(normal_count, saekyak_count)
