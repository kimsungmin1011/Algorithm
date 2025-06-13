import heapq

n, m = map(int, input().split())

final_answer = []

johap = []
visited = [False for _ in range(n + 1)]


def dfs(idx, count):
    if count == m:
        final_answer.append(johap[:])
        return

    for i in range(idx, n + 1):
        if visited[i] == False:
            visited[i] = True
            johap.append(i)
            dfs(i + 1, count + 1)
            visited[i] = False
            johap.pop()


dfs(1, 0)

for i in final_answer:
    print(*i)
