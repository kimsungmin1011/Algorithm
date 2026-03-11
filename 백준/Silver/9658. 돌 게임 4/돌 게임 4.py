n = int(input())

dp = [0 for _ in range(1001)]
# 가져갈 수 있는 돌은 1, 3, 4개
dp[1] = 0  # 상근이 패
dp[2] = 1  # 창영이 패
dp[3] = 0  # 상근이 패
dp[4] = 1  # 창영이 패

for i in range(5, n + 1):
    for number in [1, 3, 4]:
        if i - number >= 0 and dp[i - number] == 0:
            dp[i] = 1

if dp[n] == 0:
    print("CY")
else:
    print("SK")
