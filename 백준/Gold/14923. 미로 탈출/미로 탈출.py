import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]

hx, hy = map(int, input().split())
queue = deque([(hx - 1, hy - 1, 0, 0)])
visited[hx - 1][hy - 1][0] = True

ex, ey = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = False

while queue:
    x, y, time, chance = queue.popleft()
    if x == ex - 1 and y == ey - 1:
        flag = True
        print(time)
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and visited[nx][ny][chance] == False:
                visited[nx][ny][chance] = True
                queue.append((nx, ny, time + 1, chance))
            elif graph[nx][ny] == 1 and visited[nx][ny][1] == False and chance == 0:
                visited[nx][ny][1] = True
                queue.append((nx, ny, time + 1, 1))

if flag == False:
    print(-1)
