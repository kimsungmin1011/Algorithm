from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    line = list(input())
    line = [int(i) for i in line]
    graph.append(line)

visited = [[[-1 for _ in range(2)] for _ in range(m)] for _ in range(n)]

queue = deque([(0, 0, 0)])
visited[0][0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, count = queue.popleft()
    if x == n - 1 and y == m - 1:
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and visited[nx][ny][count] == -1:
                visited[nx][ny][count] = visited[x][y][count] + 1
                queue.append((nx, ny, count))
            elif graph[nx][ny] == 1 and count == 0 and visited[nx][ny][1] == -1:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, count + 1))

print(max(visited[n - 1][m - 1]))
