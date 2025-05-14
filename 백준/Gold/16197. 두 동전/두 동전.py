from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))

visited = set()

first_location = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == "o":
            first_location.append((i, j))

visited.add(tuple(sorted(first_location)))
queue = deque([(*sorted(first_location), 0)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = False
while queue:
    first_coin, second_coin, time = queue.popleft()

    if flag == True or time >= 10:
        break

    fx, fy = first_coin[0], first_coin[1]
    sx, sy = second_coin[0], second_coin[1]

    for i in range(4):
        nfx, nfy, nsx, nsy = fx + dx[i], fy + dy[i], sx + dx[i], sy + dy[i]
        if nfx >= n or nfx < 0 or nfy >= m or nfy < 0:
            if 0 <= nsx < n and 0 <= nsy < m:
                flag = True
                print(time + 1)
                break

        elif nsx >= n or nsx < 0 or nsy >= m or nsy < 0:
            if 0 <= nfx < n and 0 <= nfy < m:
                flag = True
                print(time + 1)
                break

        elif 0 <= nfx < n and 0 <= nfy < m and 0 <= nsx < n and 0 <= nsy < m:
            if graph[nfx][nfy] == "#":
                nfx, nfy = fx, fy

            if graph[nsx][nsy] == "#":
                nsx, nsy = sx, sy

            if tuple(sorted(((nfx, nfy), (nsx, nsy)))) not in visited:
                visited.add(tuple(sorted(((nfx, nfy), (nsx, nsy)))))
                queue.append((*sorted(((nfx, nfy), (nsx, nsy))), time + 1))

if flag == False:
    print(-1)
