from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_distance = 0


def bfs(x, y):
    global max_distance
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    queue = deque([(x, y, 0)])
    while queue:
        a, b, d = queue.popleft()
        max_distance = max(max_distance, d)

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] == "L":
                    visited[nx][ny] = True
                    queue.append((nx, ny, d + 1))


for i in range(n):
    for i2 in range(m):
        if graph[i][i2] == "L":
            bfs(i, i2)

print(max_distance)
