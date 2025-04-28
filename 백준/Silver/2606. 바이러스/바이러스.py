n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n + 1)]
visited[1] = True
count = 0


def dfs(node):
    global count
    for next in graph[node]:
        if visited[next] == False:
            visited[next] = True
            count += 1
            dfs(next)


dfs(1)

print(count)
