import math

# 입력 받기
n = int(input())

# DP 테이블 초기화
dp = [i for i in range(n + 1)]  # 최악의 경우: 1^2로만 구성

for i in range(1, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - j**2] + 1)

print(dp[n])
