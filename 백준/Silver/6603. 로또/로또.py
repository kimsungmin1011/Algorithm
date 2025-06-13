def dfs(idx, count, visited, current, k, line):
    if count == 6:
        print(*current)
        return

    for i in range(idx, k):
        if visited[i] == False:
            visited[i] = True
            current.append(line[i])
            dfs(i + 1, count + 1, visited, current, k, line)
            current.pop()
            visited[i] = False


while True:
    line = list(map(int, input().split()))
    k = line.pop(0)

    if k == 0:
        break

    visited = [False for _ in range(k)]
    current = []

    dfs(0, 0, visited, current, k, line)
    print()
