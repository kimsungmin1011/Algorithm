import sys

input = sys.stdin.readline

r, c = map(int, input().split())

graph = []

visited = [False] * 26

for i in range(r):
    graph.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_value = -int(1e9)


def dfs(x, y, depth):
    global max_value
    max_value = max(max_value, depth)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if visited[ord(graph[nx][ny]) - 65] == False:
                visited[ord(graph[nx][ny]) - 65] = True
                dfs(nx, ny, depth + 1)
                visited[ord(graph[nx][ny]) - 65] = False


visited[ord(graph[0][0]) - 65] = True

dfs(0, 0, 1)

print(max_value)
