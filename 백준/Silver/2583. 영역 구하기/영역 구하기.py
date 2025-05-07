from collections import deque

m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

for _ in range(k):
    start_x, start_y, end_x, end_y = map(int, input().split())

    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            graph[m - 1 - i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    queue = deque([(a, b)])
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == False and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    count += 1
                    queue.append((nx, ny))
    return count


area_count = 0
size = []

for i in range(m):
    for j in range(n):
        if visited[i][j] == False and graph[i][j] == 0:
            visited[i][j] = True
            area_count += 1
            current = bfs(i, j)
            size.append(current)

print(area_count)
print(*list(sorted(size)))
