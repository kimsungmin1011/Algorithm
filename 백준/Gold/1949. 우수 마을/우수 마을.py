import sys

sys.setrecursionlimit(10**6)

n = int(input())
people = list(map(int, input().split()))

tree = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

dp = [[0 for _ in range(2)] for _ in range(n)]

for i in range(n):
    dp[i][1] = people[i]

visited = [False for _ in range(n)]


def dfs(idx):
    for next in tree[idx]:
        if visited[next] == False:
            visited[next] = True
            dfs(next)
            dp[idx][0] += max(dp[next][0], dp[next][1])
            dp[idx][1] += dp[next][0]


visited[0] = True
dfs(0)

print(max(dp[0]))
