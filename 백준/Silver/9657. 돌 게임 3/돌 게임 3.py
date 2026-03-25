n = int(input())

# dp[i] = i개 남았을 때 현재 턴인 사람이 이기면 True, 지면 False
dp = [False for _ in range(n + 1)]

for i in range(n + 1):
    for j in [1, 3, 4]:
        if dp[i] == False and i + j <= n:
            dp[i + j] = True

if dp[n] == True:
    print("SK")
else:
    print("CY")
