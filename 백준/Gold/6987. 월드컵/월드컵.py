import sys

input = sys.stdin.readline


# 각 국가별 경기 목록 (국가 인덱스로 저장함)
match_list = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5],
    [2, 3],
    [2, 4],
    [2, 5],
    [3, 4],
    [3, 5],
    [4, 5],
]

result = []


def dfs(idx):
    global flag
    if idx == 15:
        for i in range(6):
            for j in range(3):
                if current_result[i][j] != 0:
                    return
        flag = True
        return

    match1, match2 = match_list[idx]
    for j in range(3):
        if current_result[match1][j] > 0 and current_result[match2][2 - j] > 0:
            current_result[match1][j] -= 1
            current_result[match2][2 - j] -= 1
            dfs(idx + 1)
            current_result[match1][j] += 1
            current_result[match2][2 - j] += 1


for _ in range(4):
    line = list(map(int, input().split()))
    current_result = []
    for i in range(0, 18, 3):
        current_result.append(line[i : i + 3])

    flag = False
    dfs(0)

    if flag == True:
        result.append(1)
    else:
        result.append(0)

print(*result)
