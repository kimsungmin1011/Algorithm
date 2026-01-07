import copy

n, m, t = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sx, ex = 0, 0
check = False

for i in range(n):
    if graph[i][0] == -1:
        if check == False:
            sx = i
            check = True
        else:
            ex = i


def clean(sx, ex, graph):
    # 위쪽 공기청정기(반시계)
    for x in range(sx - 1, 0, -1):
        graph[x][0] = graph[x - 1][0]
    for y in range(0, m - 1):
        graph[0][y] = graph[0][y + 1]
    for x in range(0, sx):
        graph[x][m - 1] = graph[x + 1][m - 1]
    for y in range(m - 1, 1, -1):
        graph[sx][y] = graph[sx][y - 1]
    graph[sx][1] = 0
    graph[sx][0] = -1

    # 아래쪽 공기청정기(시계)
    for x in range(ex + 1, n - 1):
        graph[x][0] = graph[x + 1][0]
    for y in range(0, m - 1):
        graph[n - 1][y] = graph[n - 1][y + 1]
    for x in range(n - 1, ex, -1):
        graph[x][m - 1] = graph[x - 1][m - 1]
    for y in range(m - 1, 1, -1):
        graph[ex][y] = graph[ex][y - 1]
    graph[ex][1] = 0
    graph[ex][0] = -1

    return graph    


for _ in range(t):
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                count = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != -1:
                        count += 1
                        new_graph[nx][ny] += graph[i][j] // 5

                new_graph[i][j] -= (graph[i][j] // 5) * count

    graph = clean(sx, ex, new_graph)


value = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
            value += graph[i][j]

print(value)
