n = int(input())
number = list(map(int, input().split()))

dp = [1 for _ in range(n)]
last = [i for i in range(n)]

for i in range(n):
    for j in range(i):
        if number[i] > number[j]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                last[i] = j

idx = 0
for i in range(1, n):
    if dp[i] > dp[idx]:
        idx = i

print(dp[idx])

answer = []
while True:
    answer.append(number[idx])
    if idx != last[idx]:
        idx = last[idx]
    else:
        break

print(*reversed(answer))
