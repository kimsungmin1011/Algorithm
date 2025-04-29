from collections import deque

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    def bfs(x, y):
        queue = deque([(x, y)])
        while queue:
            a, b = queue.popleft()
            for i in range(4):
                nx, ny = a + dx[i], b + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == False and graph[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

    count = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and graph[i][j] == 1:
                visited[i][j] = True
                count += 1
                bfs(i, j)

    print(count)
