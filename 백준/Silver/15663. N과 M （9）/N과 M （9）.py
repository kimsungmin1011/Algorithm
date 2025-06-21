n, m = map(int, input().split())
number = list(map(int, input().split()))
visited = [False for _ in range(n)]

save = set()
current = []


def dfs(count):
    if count == m:
        save.add(tuple(current))
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            current.append(number[i])
            dfs(count + 1)
            current.pop()
            visited[i] = False


dfs(0)

for i in sorted(list(save)):
    print(*i)
