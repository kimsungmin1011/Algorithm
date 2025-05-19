from collections import deque

n, l, r = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    global flag, visited, graph
    queue = deque([(a, b)])
    visited[a][b] = True
    total = graph[a][b]
    num = 1
    nation_list = [(a, b)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if (
                    l <= abs(graph[nx][ny] - graph[x][y]) <= r
                    and visited[nx][ny] == False
                ):
                    flag = True
                    visited[nx][ny] = True
                    total += graph[nx][ny]
                    num += 1
                    queue.append((nx, ny))
                    nation_list.append((nx, ny))

    for i1, i2 in nation_list:
        graph[i1][i2] = total // num


count = 0
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                bfs(i, j)

    if flag == False:
        print(count)
        break
    else:
        count += 1
