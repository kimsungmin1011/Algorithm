n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n + 1)]


def dfs(node):
    for next in graph[node]:
        if visited[next] == False:
            visited[next] = True
            dfs(next)


count = 0

for i in range(1, n + 1):
    if visited[i] == False:
        visited[i] = True
        dfs(i)
        count += 1

print(count)
