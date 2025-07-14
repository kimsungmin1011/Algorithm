n = int(input())
scv = list(map(int, input().split()))
scv.extend([0, 0])  # 3개 미만일 때 0으로 패딩

# 각 위치에 도달하는 최소 공격 횟수 저장
dp = [[[int(1e9)] * 61 for _ in range(61)] for _ in range(61)]
dp[scv[0]][scv[1]][scv[2]] = 0  # 초기 상태의 공격 횟수는 0

comb = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]

for i in range(scv[0], -1, -1):
    for j in range(scv[1], -1, -1):
        for k in range(scv[2], -1, -1):
            if dp[i][j][k] < int(1e9):  # 도달 가능한 상태만 처리
                for c in comb:
                    i_ = max(0, i - c[0])
                    j_ = max(0, j - c[1])
                    k_ = max(0, k - c[2])
                    dp[i_][j_][k_] = min(dp[i_][j_][k_], dp[i][j][k] + 1)

print(dp[0][0][0])
