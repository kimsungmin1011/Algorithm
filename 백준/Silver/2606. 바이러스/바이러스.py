from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    infected = 0
    while queue:
        v = queue.popleft()
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                infected += 1
    return infected
                
n = int(input())
graph = [[] for _ in range(n+1)]
m = int(input())

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
print(bfs(graph,1,visited))
