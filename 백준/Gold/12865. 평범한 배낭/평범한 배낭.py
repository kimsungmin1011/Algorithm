import sys

input = sys.stdin.readline

n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

# dp[i][j] : i번째 아이템까지 고려했을 때, 배낭 용량이 j일 때 얻을 수 있는 최대 가치
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = items[i - 1]  # i번째 아이템(실제로는 인덱스 i-1)
    for j in range(k + 1):
        if j < w:
            # 현재 아이템을 넣을 수 없는 경우
            dp[i][j] = dp[i - 1][j]
        else:
            # 넣는 경우 vs 안 넣는 경우 비교
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])
