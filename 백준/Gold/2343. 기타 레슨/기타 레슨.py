n, m = map(int, input().split())
lesson = list(map(int, input().split()))

left = max(lesson)
right = sum(lesson)
answer = 0

while left <= right:
    mid = (left + right) // 2
    count = 1
    weight = 0

    for i in range(n):
        if weight + lesson[i] > mid:
            weight = 0
            count += 1

        weight += lesson[i]

    if count > m:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)
