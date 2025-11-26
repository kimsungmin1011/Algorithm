from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(input()))

visited = [[False for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue2 = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == "J":
            queue1 = deque([(i, j, 0)])
            visited[i][j] = True
        elif graph[i][j] == "F":
            queue2.append((i, j, 0))

flag = False

while queue1:
    x, y, turn = queue1.popleft()

    while queue2 and turn > queue2[0][2]:
        r, l, t = queue2.popleft()
        for i in range(4):
            nr, nl = r + dx[i], l + dy[i]
            if 0 <= nr < n and 0 <= nl < m and graph[nr][nl] != "#":
                if graph[nr][nl] != "F":
                    graph[nr][nl] = "F"
                    queue2.append((nr, nl, t + 1))

    if graph[x][y] == "F":
        continue

    if x == 0 or x == n - 1 or y == 0 or y == m - 1:
        flag = True
        print(turn + 1)
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != "#":
            if graph[nx][ny] == "." and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue1.append((nx, ny, turn + 1))

if flag == False:
    print("IMPOSSIBLE")
