# 입력 받기
str1 = input().strip()
str2 = input().strip()

n, m = len(str1), len(str2)

# 첫 번째 문자열의 첫 번째 문자부터 i번째 문자까지와 두 번째 문자열의 첫 번째 문자부터 j번째 문자까지의 LCS 길이
dp = [[""] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i - 1] == str2[j - 1]:  # 문자가 같으면
            dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
        else:  # 문자가 다르면
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[n][m]))
print(dp[n][m])
