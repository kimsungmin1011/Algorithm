from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    visited[a][b] = True
    queue = deque([(a, b)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

            elif 0 <= nx < n and ny == -1:
                ny = m - 1
                if visited[nx][ny] == False and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

            elif 0 <= nx < n and ny == m:
                ny = 0
                if visited[nx][ny] == False and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

            elif nx == -1 and 0 <= ny < m:
                nx = n - 1
                if visited[nx][ny] == False and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

            elif nx == n and 0 <= ny < m:
                nx = 0
                if visited[nx][ny] == False and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == False:
            count += 1
            bfs(i, j)

print(count)
