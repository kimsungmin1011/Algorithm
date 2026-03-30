# 목표: 앱 몇 개를 비활성화 하여 M 바이트 이상의 메모리를 추가로 확보
n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

# dp[x][y] = x번째 앱에서 y비용일 때의 최대 메모리
dp = [[0 for _ in range(10001)] for _ in range(n)]
dp[0][cost[0]] = memory[0]

for i in range(1, n):
    cm, cc = memory[i], cost[i]  # 현재 앱 메모리, 비용
    for j in range(10001):
        # 앱 비활성화하지 않더라도 이전 값 이어받아야 함
        dp[i][j] = dp[i - 1][j]
        if j >= cc:
            # 앱 비활성화 하지 않는 경우, 한 경우
            dp[i][j] = max(dp[i][j], dp[i - 1][j - cc] + cm)

# 메모리 m 넘을 때 최소 비용
answer = int(1e9)
for i in range(n):
    for j in range(10001):
        if dp[i][j] >= m:
            answer = min(answer, j)

print(answer)
