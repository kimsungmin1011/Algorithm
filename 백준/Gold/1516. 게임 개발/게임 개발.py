n = int(input())

buildings = [[]]
for i in range(n):
    buildings.append(list(map(int, input().split())))

dp = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]


def dfs(idx):
    visited[idx] = True
    l = len(buildings[idx])
    t = buildings[idx][0]
    dp[idx] = t
    for i in range(1, l - 1):
        before = buildings[idx][i]
        if visited[before] == False:
            dfs(before)
        dp[idx] = max(dp[idx], dp[before] + t)


for i in range(1, n + 1):
    if visited[i] == False:
        dfs(i)

for i in range(1, n + 1):
    print(dp[i])
