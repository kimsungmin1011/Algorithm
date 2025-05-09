from collections import deque

r, c = map(int, input().split())

graph = []

for i in range(r):
    line = list(input())
    graph.append([i for i in line])

visited = [[-1 for _ in range(c)] for _ in range(r)]
queue = deque([])

for i in range(r):
    for j in range(c):
        if graph[i][j] == "*":
            queue.append((i, j, "*"))
        elif graph[i][j] == "D":
            d_x, d_y = i, j

for i in range(r):
    for j in range(c):
        if graph[i][j] == "S":
            queue.append((i, j, "S"))
            visited[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, current = queue.popleft()
    if current == "*":
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == "." and visited[nx][ny] == -1:
                    visited[nx][ny] = False
                    queue.append((nx, ny, "*"))

    elif current == "S":
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if (graph[nx][ny] == "." or graph[nx][ny] == "D") and visited[nx][
                    ny
                ] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny, "S"))

if visited[d_x][d_y] == -1:
    print("KAKTUS")
else:
    print(visited[d_x][d_y])
