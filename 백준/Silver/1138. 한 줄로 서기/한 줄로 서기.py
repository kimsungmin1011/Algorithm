n = int(input())
line = list(map(int, input().split()))
rank = [0] * n

for i in range(n):
    number = line[i]
    count = 0
    for x in range(n):
        if count == number:
            if rank[x] == 0:
                rank[x] = i + 1
                break
        if rank[x] == 0 or rank[x] > i + 1:
            count += 1

print(*rank)
