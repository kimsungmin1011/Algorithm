from collections import deque

m, n = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]
queue = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            visited[i][j] = True
            queue.append((i, j, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
last_day = 0

while queue:
    x, y, time = queue.popleft()
    last_day = max(last_day, time)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and graph[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, time + 1))

flag = True
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == False:
            flag = False
            break

if flag == True:
    print(last_day)
else:
    print(-1)
