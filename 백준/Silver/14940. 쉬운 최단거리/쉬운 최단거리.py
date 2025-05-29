from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            queue = deque([(i, j)])

visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] == 1:
            visited[i][j] = -1

for line in visited:
    print(*line)
