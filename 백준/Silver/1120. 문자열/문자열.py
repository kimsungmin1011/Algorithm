first, last = input().split()

min_count = float("inf")

# A를 B에 맞춰 이동시키며 비교
for i in range(len(last) - len(first) + 1):
    count = 0
    for j in range(len(first)):
        if first[j] != last[i + j]:
            count += 1
    min_count = min(min_count, count)

print(min_count)
