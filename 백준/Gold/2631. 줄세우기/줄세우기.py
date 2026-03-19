import sys

input = sys.stdin.readline

n = int(input())

num = []
for i in range(n):
    num.append(int(input()))

dp = [1] * (n + 1)

# 가장 긴 증가하는 수열 찾기
for i in range(n):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# n- 긴 증가하는 부분수열의 길이
print(n - max(dp))
