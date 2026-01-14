graph = []

for i in range(19):
    graph.append(list(map(int, input().split())))

visited = [[[False for _ in range(4)] for _ in range(19)] for _ in range(19)]


def check(x, y):
    current = graph[x][y]

    count = 0
    i = 0
    while True:
        if x + i < 19 and graph[x + i][y] == current and visited[x + i][y][0] == False:
            visited[x + i][y][0] = True
            i += 1
            count += 1
        else:
            break

    if count == 5:
        return True

    count = 0
    i = 0
    while True:
        if y + i < 19 and graph[x][y + i] == current and visited[x][y + i][1] == False:
            visited[x][y + i][1] = True
            i += 1
            count += 1
        else:
            break

    if count == 5:
        return True

    count = 0
    i = 0
    while True:
        if (
            x + i < 19
            and y + i < 19
            and graph[x + i][y + i] == current
            and visited[x + i][y + i][2] == False
        ):
            visited[x + i][y + i][2] = True
            i += 1
            count += 1
        else:
            break

    if count == 5:
        return True

    count = 0
    i = 0
    while True:
        if (
            0 <= x - i
            and y + i < 19
            and graph[x - i][y + i] == current
            and visited[x - i][y + i][3] == False
        ):
            visited[x - i][y + i][3] = True
            i += 1
            count += 1
        else:
            break

    if count == 5:
        return True


for j in range(19):
    for i in range(19):
        if graph[i][j] != 0 and check(i, j):
            print(graph[i][j])
            print(i + 1, j + 1)
            exit()

print(0)
