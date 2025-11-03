n, m = map(int, input().split())
lesson = list(map(int, input().split()))

left = 1
right = sum(lesson)
answer = sum(lesson)

while left <= right:
    mid = (left + right) // 2
    count = 1
    weight = 0
    flag = True

    for i in range(n):
        if lesson[i] > mid:
            flag = False
            break

        if weight + lesson[i] > mid:
            weight = 0
            count += 1

        weight += lesson[i]

    if flag == False or count > m:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)
