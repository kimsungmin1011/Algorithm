n = int(input())
works = []
for _ in range(n):
    works.append(list(map(int, input().split())))

# dp[x] = x번째 작업이 완료되기 위한 최소시간
dp = [0 for _ in range(n)]
dp[0] = works[0][0]

for i in range(1, n):
    dp[i] = works[i][0]
    amount = works[i][1]

    new_value = works[i][0]
    for j in range(2, 2 + amount):
        new_value = max(new_value, dp[i] + dp[works[i][j] - 1])
        
    dp[i] = max(dp[i], new_value)

print(max(dp))
