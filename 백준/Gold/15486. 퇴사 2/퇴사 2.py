import sys

input = sys.stdin.readline

N = int(input())  # 전체 날짜 수
schedule = [list(map(int, input().split())) for i in range(N)]  # [T, P] 리스트 입력
dp = [0 for i in range(N + 1)]  # i일까지의 최대 수익

# i번째 날짜에 대해 처리
for i in range(N):
    # 현재 상담을 진행하지 않는 경우, 다음 날로 수익을 넘김
    dp[i + 1] = max(dp[i + 1], dp[i])

    # 현재 상담을 진행할 수 있는 경우, i + T[i] 날에 수익을 반영
    if i + schedule[i][0] <= N:  # 퇴사일 이후를 초과하지 않아야 함
        dp[i + schedule[i][0]] = max(dp[i + schedule[i][0]], dp[i] + schedule[i][1])

print(max(dp))  # dp 배열의 최대값 출력
