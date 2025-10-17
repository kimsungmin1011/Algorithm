from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())

visited = [[False for _ in range(m)] for _ in range(n)]

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

queue = deque()

if d == 1:
    queue.append((r, c, 3, 1))
elif d == 3:
    queue.append((r, c, 1, 1))
else:
    queue.append((r, c, d, 1))

visited[r][c] = True
answer = 1

while queue:
    x, y, cd, count = queue.popleft()
    flag = False

    # 인접 4칸 중에 아직 방문 안 한 칸 있으면 전진
    for i in range(1, 5):
        nd = (cd + i) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                flag = True
                visited[nx][ny] = True
                queue.append((nx, ny, nd, count + 1))
                break

    # 없으면 방향 유지한 채 뒤로 빠꾸
    if flag == False:
        nx, ny = x - dx[cd], y - dy[cd]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            # 만약 빠꾸한 칸이 아직 방문 안 한 칸이라면
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny, cd, count + 1))
            else:
                queue.append((nx, ny, cd, count))
        else:
            answer = count

print(answer)
