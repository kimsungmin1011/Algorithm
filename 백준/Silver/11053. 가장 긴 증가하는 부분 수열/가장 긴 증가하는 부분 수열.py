n = int(input())
a = list(map(int, input().split()))

dp = [1 for _ in range(n)]  # i 인덱스까지 가장 긴 증가하는 부분수열

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))
