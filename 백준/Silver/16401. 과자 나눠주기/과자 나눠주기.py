m, n = map(int, input().split())
snacks = list(map(int, input().split()))
snacks.sort()

start = 1
end = max(snacks)
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for snack in snacks:
        while snack >= mid:
            count += 1
            snack -= mid

    if count >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
