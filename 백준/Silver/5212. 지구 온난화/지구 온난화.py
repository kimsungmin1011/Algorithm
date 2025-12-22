import copy

r, c = map(int, input().split())
graph = []

for _ in range(r):
    graph.append(list(input()))

new_graph = copy.deepcopy(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

big_x, big_y, small_x, small_y = 0, 0, int(1e9), int(1e9)

for i in range(r):
    for j in range(c):
        if graph[i][j] == "X":
            count = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if nx >= r or nx < 0 or ny >= c or ny < 0:
                    count += 1
                    continue
                if graph[nx][ny] == ".":
                    count += 1
            if count >= 3:
                flag = True
                new_graph[i][j] = "."

for i in range(r):
    for j in range(c):
        if new_graph[i][j] == "X":
            big_x = max(big_x, i)
            big_y = max(big_y, j)
            small_x = min(small_x, i)
            small_y = min(small_y, j)

for i in range(small_x, big_x + 1):
    for j in range(small_y, big_y + 1):
        print(new_graph[i][j], end="")
    print()
