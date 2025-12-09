import sys
from collections import deque  # 안 써도 되지만 놔둠

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]   # 0: 위, 1: 아래, 2: 왼, 3: 오른쪽
dy = [0, 0, -1, 1]

visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
real = [[False for _ in range(m)] for _ in range(n)]

aircons = []
count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 9:
            count += 1
            real[i][j] = True
            aircons.append((i, j))

# 에어컨마다, 4방향 레이 쏘기
for sx, sy in aircons:
    for d in range(4):
        x, y, dir = sx, sy, d

        while True:
            # 이미 이 칸에 이 방향으로 온 적 있으면 종료 (사이클 방지)
            if visited[x][y][dir]:
                break
            visited[x][y][dir] = True

            # 바람이 실제로 지난 자리 카운트
            if not real[x][y]:
                real[x][y] = True
                count += 1

            t = graph[x][y]

            # 다음 위치/방향 계산
            if t == 0 or t == 9:
                nx = x + dx[dir]
                ny = y + dy[dir]
                ndir = dir
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                x, y, dir = nx, ny, ndir

            elif t == 1:
                if dir == 2:  # 왼쪽으로 가던 바람 → 오른쪽으로 튕김
                    ny = y + 1
                    if not (0 <= ny < m):
                        break
                    nx = x
                    ndir = 3
                elif dir == 3:  # 오른쪽으로 가던 바람 → 왼쪽으로 튕김
                    ny = y - 1
                    if not (0 <= ny < m):
                        break
                    nx = x
                    ndir = 2
                else:  # 위/아래는 직진
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    ndir = dir
                    if not (0 <= nx < n and 0 <= ny < m):
                        break
                x, y, dir = nx, ny, ndir

            elif t == 2:
                if dir == 0:  # 위로 가던 바람 → 아래로 튕김
                    nx = x + 1
                    ny = y
                    ndir = 1
                    if not (0 <= nx < n):
                        break
                elif dir == 1:  # 아래로 가던 바람 → 위로 튕김
                    nx = x - 1
                    ny = y
                    ndir = 0
                    if not (0 <= nx < n):
                        break
                else:  # 좌/우는 직진
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    ndir = dir
                    if not (0 <= nx < n and 0 <= ny < m):
                        break
                x, y, dir = nx, ny, ndir

            elif t == 3:
                if dir == 0:  # 위 → 오른쪽
                    nx = x
                    ny = y + 1
                    ndir = 3
                    if not (0 <= ny < m):
                        break
                elif dir == 1:  # 아래 → 왼쪽
                    nx = x
                    ny = y - 1
                    ndir = 2
                    if not (0 <= ny < m):
                        break
                elif dir == 2:  # 왼쪽 → 아래
                    nx = x + 1
                    ny = y
                    ndir = 1
                    if not (0 <= nx < n):
                        break
                elif dir == 3:  # 오른쪽 → 위
                    nx = x - 1
                    ny = y
                    ndir = 0
                    if not (0 <= nx < n):
                        break
                x, y, dir = nx, ny, ndir

            elif t == 4:
                if dir == 0:  # 위 → 왼쪽
                    nx = x
                    ny = y - 1
                    ndir = 2
                    if not (0 <= ny < m):
                        break
                elif dir == 1:  # 아래 → 오른쪽
                    nx = x
                    ny = y + 1
                    ndir = 3
                    if not (0 <= ny < m):
                        break
                elif dir == 2:  # 왼쪽 → 위
                    nx = x - 1
                    ny = y
                    ndir = 0
                    if not (0 <= nx < n):
                        break
                elif dir == 3:  # 오른쪽 → 아래
                    nx = x + 1
                    ny = y
                    ndir = 1
                    if not (0 <= nx < n):
                        break
                x, y, dir = nx, ny, ndir

print(count)
