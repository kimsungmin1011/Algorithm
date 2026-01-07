h, w = map(int, input().split())
graph = [[0 for _ in range(w)] for _ in range(h)]
wall = list(map(int, input().split()))

for i in range(w):
    height = wall[i]
    for j in range(h - height, h):
        graph[j][i] = 1

count = 0

for i in range(h):
    for j in range(w):
        if graph[i][j] == 0:
            check = 0
            for l in range(j):
                if graph[i][l] == 1:
                    check += 1
                    break

            for r in range(j + 1, w):
                if graph[i][r] == 1:
                    check += 1
                    break

            if check == 2:
                count += 1

print(count)
