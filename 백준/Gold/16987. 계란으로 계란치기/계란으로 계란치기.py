import sys

input = sys.stdin.readline

n = int(input())
egg = []

for i in range(n):
    egg.append(list(map(int, input().split())))

max_broke = 0


def dfs(idx, count):
    global max_broke
    max_broke = max(max_broke, count)
    # 모든 계란을 다 탐색함
    if idx == n:
        return

    # 현재 계란이 이미 깨졌다면 다음 계란으로
    if egg[idx][0] <= 0:
        dfs(idx + 1, count)
        return

    current_weight = egg[idx][1]  # 현재 계란의 무게

    for i in range(n):
        if i == idx or egg[i][0] <= 0:
            # 때리려는 계란이 현재 들고있는 계란이거나 내구도가 0 이하라면 넘김
            continue
        egg[i][0] -= current_weight  # 현재 계란으로 다른 계란 치기
        egg[idx][0] -= egg[i][1]  # 현재 계란도 때린 계란의 무게만큼 내구도 줄어듬

        if egg[i][0] <= 0 and egg[idx][0] <= 0:
            # 둘 다 깨짐
            dfs(idx + 1, count + 2)
        elif egg[i][0] <= 0 or egg[idx][0] <= 0:
            # 한 개만 깨짐
            dfs(idx + 1, count + 1)
        else:
            # 하나도 안 깨짐
            dfs(idx + 1, count)
        # 원복
        egg[i][0] += current_weight
        egg[idx][0] += egg[i][1]


dfs(0, 0)

print(max_broke)
