n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(idx, count):
    if count == 4:
        return True

    for i in graph[idx]:
        if visited[i] == False:
            visited[i] = True
            if dfs(i, count + 1) == True:
                return True
            visited[i] = False

    return False


flag = False
for i in range(n):
    visited = [False for _ in range(n)]
    visited[i] = True
    if dfs(i, 0) == True:
        flag = True
        print(1)
        break

if flag == False:
    print(0)
