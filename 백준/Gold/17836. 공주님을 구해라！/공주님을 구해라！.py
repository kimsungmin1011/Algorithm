from collections import deque

n, m, t = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[[int(1e9) for _ in range(2)] for _ in range(m)] for _ in range(n)]
queue = deque([(0, 0, 0, 0)])
visited[0][0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = False
while queue:
    x, y, time, check = queue.popleft()

    if time > t:
        break

    if x == n - 1 and y == m - 1:
        flag = True
        print(visited[x][y][check])
        break

    if graph[x][y] == 2:
        check = 1
        visited[x][y][1] = visited[x][y][0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (
            0 <= nx < n
            and 0 <= ny < m
            and ((check == 0 and graph[nx][ny] != 1) or check == 1)
            and visited[nx][ny][check] > visited[x][y][check] + 1
        ):
            visited[nx][ny][check] = visited[x][y][check] + 1
            queue.append((nx, ny, time + 1, check))

if flag == False:
    print("Fail")
