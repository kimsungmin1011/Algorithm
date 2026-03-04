r, c, n = map(int, input().split())
graph = []

for i in range(r):
    graph.append(list(input()))

# 폭탄 설치한 곳 시간
time = [[0 for _ in range(c)] for _ in range(r)]

current = 1

# 폭탄 범위
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

while current <= n:
    # 폭탄 설치한 곳 시간 + 1 & 폭발 (이번에 새로 설치한 곳 제외)
    bye = set()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "O":
                time[i][j] += 1
                if time[i][j] == 3:
                    for k in range(5):
                        nx, ny = i + dx[k], j + dy[k]
                        if 0 <= nx < r and 0 <= ny < c:
                            bye.add((nx, ny))

    # 한번에 폭발
    for x, y in list(bye):
        graph[x][y] = "."
        time[x][y] = 0

    # 폭탄 설치 (봄버맨은 짝수 시간에만 폭탄 설치)
    if current != 0 and current % 2 == 0:
        for i in range(r):
            for j in range(c):
                if graph[i][j] == ".":
                    graph[i][j] = "O"

    current += 1

for line in graph:
    for i in line:
        print(i, end="")
    print()
