from collections import deque

m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))

queue = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k, 0))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

last_day = 0

while queue:
    x, y, z, time = queue.popleft()
    last_day = time

    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
            if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                visited[nx][ny][nz] = True
                queue.append((nx, ny, nz, time + 1))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0 and visited[i][j][k] == False:
                print(-1)
                exit()

print(last_day)
