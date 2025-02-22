n = int(input())
# dp[현재 추 인덱스][무게] = 가능(1), 불가능(0)
dp = [[0 for _ in range(40001)] for _ in range(n + 1)]
stone = list(map(int, input().split()))

m = int(input())
ball = list(map(int, input().split()))

for i in range(1, n + 1):
    c_stone = stone[i - 1]
    dp[i][c_stone] = 1
    for j in range(15001):
        if dp[i - 1][j] == 1:
            dp[i][j] = 1
            if j + c_stone <= 15000:
                dp[i][j + c_stone] = 1
            if abs(j - c_stone) <= 15000:
                dp[i][abs(j - c_stone)] = 1

answer = []
for j in ball:
    flag = False
    for i in range(1, n + 1):
        if dp[i][j] == 1:
            flag = True
            answer.append("Y")
            break
    if flag == False:
        answer.append("N")

for i in answer:
    print(i, end=" ")
