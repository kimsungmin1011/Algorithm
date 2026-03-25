n = int(input())

# dp[i] = i개 남았을 때 현재 턴인 사람이 이기면 True, 지면 False
dp = [False for _ in range(n + 1)]

for i in range(n + 1):
    for j in [1, 3, 4]:
        if 0 <= i - j <= n:
            if dp[i - j] == False:
                dp[i] = True
                break


# 상근이가 n개인 상태에서 먼저 시작
if dp[n] == True:
    print("SK")
else:
    print("CY")
