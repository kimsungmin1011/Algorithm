n = int(input())
sangdam = []

sangdam.append((0, 0))
for i in range(n):
    sangdam.append(list(map(int, input().split())))

# dp[i] = i번째 되는 날의 최대수익
dp = [0 for _ in range(n + 2)]

# n일동안 상담 잡기
for i in range(1, n + 1):
    ctime, cpay = sangdam[i][0], sangdam[i][1]  # i일에 잡혀있는 상담시간, 금액
    dp[i] = max(dp[i], dp[i - 1])  # 현재 수익과 전날 수익을 비교함

    if i + ctime <= n + 1:
        # 퇴사일 이내면 갱신
        # dp[현재 상담 끝난 날] = max(dp[현재 상담 끝난 날], dp[오늘]+현재상담금액)
        dp[i + ctime] = max(dp[i + ctime], dp[i] + cpay)

dp[n + 1] = max(dp[n + 1], dp[n])  # 퇴사일 최대 수익 갱신 (퇴사 전날 vs 퇴사당일)
print(dp[n + 1])  # 퇴사일 최대수익 (퇴사일에 상담 안 해도 이전 최대수익 가져옴)
