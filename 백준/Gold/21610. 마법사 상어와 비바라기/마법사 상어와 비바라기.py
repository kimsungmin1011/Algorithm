import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

directions = []

for _ in range(m):
    directions.append(list(map(int, input().split())))

# 8방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 초기 구름 위치
cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

# M번 이동 반복
for i in range(m):
    d, s = directions[i][0], directions[i][1]  # d 방향으로 s칸 이동
    d -= 1  # 방향 조정

    # 구름 이동 (1번 행과 N번 행, 1번 열과 N번 열 연결함)
    for i2 in range(len(cloud)):
        cloud[i2][0] = (cloud[i2][0] + dx[d] * s) % n
        cloud[i2][1] = (cloud[i2][1] + dy[d] * s) % n

    # 구름에 비 내림
    for x, y in cloud:
        graph[x][y] += 1

    # 물복사버그 마법
    for x, y in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
        for i1, i2 in cloud:
            nx, ny = x + i1, y + i2
            count = 0
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                count += 1
            graph[i1][i2] += count

    # 이전에 구름 있는 칸 저장
    yesterday = set()
    for x, y in cloud:
        yesterday.add((x, y))

    cloud = []  # 구름 없어짐

    for i2 in range(n):
        for j in range(n):
            # 구름이 생기는 칸은 이전에 구름 있는 칸이 아니어야 하며 2 이상
            if (i2, j) not in yesterday and graph[i2][j] >= 2:
                cloud.append([i2, j])
                graph[i2][j] -= 2

answer = 0
for i in range(n):
    answer += sum(graph[i])

print(answer)
