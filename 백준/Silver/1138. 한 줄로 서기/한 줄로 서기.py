n = int(input())
line = list(map(int, input().split()))
rank_list = [0] * n

for i in range(n):
    number = line[i]
    count = 0
    for x in range(n):
        if count == number and rank_list[x] == 0:
            rank_list[x] = i + 1
            break
        elif rank_list[x] == 0 or rank_list[x] > i + 1:
            count += 1

print(*rank_list)
