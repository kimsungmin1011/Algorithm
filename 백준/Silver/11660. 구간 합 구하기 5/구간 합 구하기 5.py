n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        dp[i][j] += graph[i][j]
        if i - 1 >= 0:
            dp[i][j] += dp[i - 1][j]
        if j - 1 >= 0:
            dp[i][j] += dp[i][j - 1]
        if i - 1 >= 0 and j - 1 >= 0:
            dp[i][j] -= dp[i - 1][j - 1]

for _ in range(m):
    sx, sy, ex, ey = map(int, input().split())
    sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1

    answer = dp[ex][ey]
    if sx - 1 >= 0:
        answer -= dp[sx - 1][ey]
    if sy - 1 >= 0:
        answer -= dp[ex][sy - 1]
    if sx - 1 >= 0 and sy - 1 >= 0:
        answer += dp[sx - 1][sy - 1]

    print(answer)
