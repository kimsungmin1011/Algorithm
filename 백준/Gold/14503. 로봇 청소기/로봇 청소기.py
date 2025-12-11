n, m = map(int, input().split())
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]

x, y, d = map(int, input().split())
if d == 3:
    d = 1
elif d == 1:
    d = 3

visited[x][y] = True

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


while True:
    flag = False
    for i in range(1, 5):
        nd = (d + i) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        if (
            0 <= nx < n
            and 0 <= ny < m
            and graph[nx][ny] == 0
            and visited[nx][ny] == False
        ):
            visited[nx][ny] = True
            x, y, d = nx, ny, nd
            flag = True
            break

    if flag == False:
        nx, ny = x - dx[d], y - dy[d]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            x, y = nx, ny
        else:
            break

count = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == True:
            count += 1

print(count)
