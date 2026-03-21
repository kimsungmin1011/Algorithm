n, d = map(int, input().split())

fast = dict()
for _ in range(n):
    start, end, l = map(int, input().split())
    if end not in fast:
        fast[end] = [(start, l)]
    else:
        fast[end].append((start, l))

dp = [0 for _ in range(d + 1)]

for current in range(1, d + 1):
    dp[current] = dp[current - 1] + 1
    if current in fast:
        for j in fast[current]:
            before, l = j[0], j[1]
            dp[current] = min(dp[current], dp[before] + l)

print(dp[d])
