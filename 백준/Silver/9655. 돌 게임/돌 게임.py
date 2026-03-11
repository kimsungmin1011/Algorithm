n = int(input())

# dp[i]는 돌이 i개 남았을 때 해당 플레이어가 승리할 수 있는지 여부
dp = [False] * (n + 1)

# 초기 상태 설정 (기저 사례)
if n >= 1:
    dp[1] = True  # 돌이 1개 남았을 때, 현재 턴인 사람이 1개 가져가면 승리
if n >= 3:
    dp[3] = True  # 돌이 3개 남았을 때, 현재 턴인 사람이 3개 가져가면 승리

# 동적 프로그래밍 진행
for i in range(2, n + 1):
    # 현재 턴인 사람이 승리하려면, 상대방에게 패배 상태를 넘겨줘야 함
    if i >= 1 and not dp[i - 1]:  # 돌 1개를 가져갈 경우 상대방이 패배 상태
        dp[i] = True
    elif i >= 3 and not dp[i - 3]:  # 돌 3개를 가져갈 경우 상대방이 패배 상태
        dp[i] = True

# 결과 출력
if dp[n]:
    print("SK")  # SK가 승리
else:
    print("CY")  # CY가 승리
