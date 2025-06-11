n, m = map(int, input().split())
answer = []

visited = [False for _ in range(n)]


def dfs(cnt, line):
    if cnt == m:
        answer.append(line)
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            dfs(cnt + 1, line + [i + 1])
            visited[i] = False


dfs(0, [])

for i in sorted(answer):
    print(*i)
