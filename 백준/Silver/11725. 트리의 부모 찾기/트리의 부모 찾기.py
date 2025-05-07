import sys

sys.setrecursionlimit(100000)

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n + 1)]
visited[1] = True
parents = [0 for _ in range(n + 1)]


def dfs(node):
    for i in graph[node]:
        if visited[i] == False:
            parents[i] = node
            visited[i] = True
            dfs(i)


dfs(1)

for i in range(2, n + 1):
    print(parents[i])
