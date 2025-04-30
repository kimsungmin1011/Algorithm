n = int(input())

graph = []

for i in range(n):
    line = list(input())
    line = [int(i) for i in line]
    graph.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for _ in range(n)] for _ in range(n)]


def dfs(x, y):
    count = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                visited[nx][ny] = True
                count += dfs(nx, ny)

    return count


answer_count = 0
answer = []

for i in range(n):
    for j in range(n):
        if visited[i][j] == False and graph[i][j] == 1:
            visited[i][j] = True
            answer_count += 1
            size = dfs(i, j)
            answer.append(size)

print(answer_count)

answer.sort()

for i in answer:
    print(i)
