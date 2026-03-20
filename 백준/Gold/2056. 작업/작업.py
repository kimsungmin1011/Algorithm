n = int(input())
works = []
for _ in range(n):
    # works[i] = [현재 작업 시간, 선행 작업 개수, 선행 작업 번호들...]
    works.append(list(map(int, input().split())))

# dp[i] = i번째 작업을 끝낼 수 있는 가장 빠른 시간
dp = [0 for _ in range(n)]
# 1번 작업은 선행 작업이 없다고 보고 자기 작업 시간으로 시작
dp[0] = works[0][0]

# 각 작업의 완료 시간을 차례대로 계산
# 선행 작업이 여러 개라면, 그중 가장 늦게 끝나는 작업 이후에 시작 가능
for i in range(1, n):
    # 현재 작업 시간 / 선행 작업 개수
    time = works[i][0]
    amount = works[i][1]
    dp[i] = time

    # 선행 작업들을 보면서
    # 현재 작업 시간 + 선행 작업 완료 시간의 최댓값을 구함
    for j in range(2, 2 + amount):
        # 가장 늦게 끝나는 선행 작업을 기준으로 완료 시간이 결정됨
        dp[i] = max(dp[i], time + dp[works[i][j] - 1])

# 모든 작업이 끝나는 전체 시간은 완료 시간들 중 최댓값
print(max(dp))
