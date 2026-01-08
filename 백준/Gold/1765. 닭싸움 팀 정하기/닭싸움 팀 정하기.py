n = int(input())
m = int(input())

friend_graph = [[] for _ in range(n + 1)]
enemy_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    line = list(input().split())
    first, second = int(line[1]), int(line[2])
    flag = line[0]

    if flag == "F":
        friend_graph[first].append(second)
        friend_graph[second].append(first)
    else:
        enemy_graph[first].append(second)
        enemy_graph[second].append(first)


# 적의적은친구다
def eef(start, node, count):
    if count > 0 and count % 2 == 0:
        if node not in friend_graph[start]:
            friend_graph[start].append(node)
        if start not in friend_graph[node]:
            friend_graph[node].append(start)

    for next in enemy_graph[node]:
        if visited[next] == False:
            visited[next] = True
            eef(start, next, count + 1)


def dfs(node):
    for next in friend_graph[node]:
        if visited[next] == False:
            visited[next] = True
            dfs(next)


for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    visited[i] = True
    eef(i, i, 0)

count = 0
visited = [False for _ in range(n + 1)]
for i in range(1, n + 1):
    if visited[i] == False:
        visited[i] = True
        count += 1
        dfs(i)

print(count)
