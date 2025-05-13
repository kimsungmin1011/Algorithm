import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, group):
    queue = deque([start])
    visited[start] = group  # 시작 노드 그룹 설정
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:  # 아직 방문하지 않았다면
                visited[i] = -visited[x]  # 현재 노드와 다른 그룹으로 설정
                queue.append(i)
            elif visited[i] == visited[x]:  # 이미 방문했고, 같은 그룹이라면
                return False
    return True


for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V + 1)]
    visited = [False] * (V + 1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)  # 무방향 그래프
        graph[b].append(a)  # 무방향 그래프

    for i in range(1, V + 1):
        if not visited[i]:  # 방문한 정점이 아니면, bfs 수행
            result = bfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")
