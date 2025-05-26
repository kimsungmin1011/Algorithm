from collections import deque

m, n = map(int, input().split())
visited = [[[int(1e11) for _ in range(4)] for _ in range(n)] for _ in range(m)]
graph = []

for i in range(m):
    graph.append(list(map(int, input().split())))

sx, sy, sd = map(int, input().split())
sx -= 1
sy -= 1
sd -= 1
visited[sx][sy][sd] = 0
queue = deque([(sx, sy, sd)])

ex, ey, ed = map(int, input().split())
ex -= 1
ey -= 1
ed -= 1


while queue:
    cx, cy, cd = queue.popleft()
    if cx == ex and cy == ey and cd == ed:
        print(visited[cx][cy][cd])
        break

    if cd == 0 or cd == 1:
        if visited[cx][cy][2] > visited[cx][cy][cd] + 1:
            visited[cx][cy][2] = visited[cx][cy][cd] + 1
            queue.append((cx, cy, 2))

        if visited[cx][cy][3] > visited[cx][cy][cd] + 1:
            visited[cx][cy][3] = visited[cx][cy][cd] + 1
            queue.append((cx, cy, 3))

    else:
        if visited[cx][cy][0] > visited[cx][cy][cd] + 1:
            visited[cx][cy][0] = visited[cx][cy][cd] + 1
            queue.append((cx, cy, 0))

        if visited[cx][cy][1] > visited[cx][cy][cd] + 1:
            visited[cx][cy][1] = visited[cx][cy][cd] + 1
            queue.append((cx, cy, 1))

    if cd == 0:
        # 동쪽으로 최대 3칸 이동
        for i in range(1, 4):
            nx, ny = cx, cy + i
            # 범위 초과 또는 벽이면 이동 중단
            if ny >= n or graph[nx][ny] == 1:
                break
            # 이미 더 적은 명령으로 방문했으면 건너뜀
            if visited[nx][ny][cd] <= visited[cx][cy][cd] + 1:
                continue
            visited[nx][ny][cd] = visited[cx][cy][cd] + 1
            queue.append((nx, ny, cd))

    if cd == 1:
        # 서쪽으로 최대 3칸 이동
        for i in range(1, 4):
            nx, ny = cx, cy - i
            if ny < 0 or graph[nx][ny] == 1:
                break
            if visited[nx][ny][cd] <= visited[cx][cy][cd] + 1:
                continue
            visited[nx][ny][cd] = visited[cx][cy][cd] + 1
            queue.append((nx, ny, cd))

    if cd == 2:
        # 남쪽으로 최대 3칸 이동
        for i in range(1, 4):
            nx, ny = cx + i, cy
            if nx >= m or graph[nx][ny] == 1:
                break
            if visited[nx][ny][cd] <= visited[cx][cy][cd] + 1:
                continue
            visited[nx][ny][cd] = visited[cx][cy][cd] + 1
            queue.append((nx, ny, cd))

    if cd == 3:
        # 북쪽으로 최대 3칸 이동
        for i in range(1, 4):
            nx, ny = cx - i, cy
            if nx < 0 or graph[nx][ny] == 1:
                break
            if visited[nx][ny][cd] <= visited[cx][cy][cd] + 1:
                continue
            visited[nx][ny][cd] = visited[cx][cy][cd] + 1
            queue.append((nx, ny, cd))
