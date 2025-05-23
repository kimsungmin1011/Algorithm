import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, start, end = map(int, input().split())
visited = [False for _ in range(n + 1)]
visited[start] = True
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

flag = False


def dfs(node):
    global distance_list
    if node == end:
        if distance_list:
            distance_list.sort()
            distance_list.pop()
            print(sum(distance_list))
        else:
            print(0)
        exit()
    for next, ndistance in graph[node]:
        if visited[next] == False:
            visited[next] = True
            distance_list.append(ndistance)
            dfs(next)
            distance_list.pop()
            visited[next] = False


distance_list = []
dfs(start)
