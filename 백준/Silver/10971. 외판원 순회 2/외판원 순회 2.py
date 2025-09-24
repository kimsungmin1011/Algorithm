n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

min_cost = int(1e9)


def dfs(count, idx, start, cost):
    global min_cost

    if count == n:
        if graph[idx][start] != 0:
            min_cost = min(min_cost, cost + graph[idx][start])
        return

    for i in range(n):
        if i != start and visited[i] == False and graph[idx][i] != 0:
            visited[i] = True
            dfs(count + 1, i, start, cost + graph[idx][i])
            visited[i] = False


for i in range(n):
    visited = [False for _ in range(n)]
    visited[i] = True
    dfs(1, i, i, 0)

print(min_cost)
