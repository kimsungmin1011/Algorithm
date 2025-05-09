from collections import deque

n, m = map(int, input().split())

ladder = {}
for i in range(n):
    a, b = map(int, input().split())
    ladder[a] = b

snakes = {}
for i in range(m):
    a, b = map(int, input().split())
    snakes[a] = b

visited = [False for _ in range(101)]
dx = [1, 2, 3, 4, 5, 6]

queue = deque([(1, 0)])
visited[1] = True

while queue:
    current, time = queue.popleft()
    if current == 100:
        print(time)
        break

    for i in range(6):
        nx = current + dx[i]
        if nx <= 100:
            if nx in ladder:
                go = ladder[nx]
                visited[go] = True
                queue.append((go, time + 1))

            elif nx in snakes:
                go = snakes[nx]
                visited[go] = True
                queue.append((go, time + 1))

            elif visited[nx] == False:
                visited[nx] = True
                queue.append((nx, time + 1))
