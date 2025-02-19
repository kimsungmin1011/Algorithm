from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(1, n + 1):
    line = list(map(int, input().split()))
    line.pop(0)
    graph[i] = line

blue_team = set()
red_team = set()


def bfs(x):
    queue = deque([(x, 1)])
    visited[x] = True
    blue_team.add(x)

    while queue:
        node, team = queue.popleft()

        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                if team == 1:
                    red_team.add(i)
                    queue.append((i, -1))

                elif team == -1:
                    blue_team.add(i)
                    queue.append((i, 1))


for i in range(1, n + 1):
    if visited[i] == False:
        bfs(i)

print(len(blue_team))
print(*sorted(blue_team))

print(len(red_team))
print(*sorted(red_team))
