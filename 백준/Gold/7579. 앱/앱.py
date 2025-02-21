n, m = map(int, input().split())

using_memory = [0]
using_memory.extend(list(map(int, input().split())))

cost = [0]
cost.extend(list(map(int, input().split())))

# dp[현재 앱 인덱스][비용] = 확보한 메모리
dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(n + 1)]

min_value = int(1e9)  # 메모리 m 이상 확보하는데 드는 비용 최솟값

for i in range(1, n + 1):
    c_using_memory, c_cost = using_memory[i], cost[i]
    for j in range(sum(cost) + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= c_cost:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - c_cost] + c_using_memory)
        if dp[i][j] >= m:  # 현재 확보한 메모리가 m 이상이면
            min_value = min(min_value, j)  # 비용 최솟값 갱신

print(min_value)
