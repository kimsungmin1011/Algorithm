n, m = map(int, input().split())
number = list(map(int, input().split()))

left, right = 0, 0
total = number[0]
answer = 0

while left <= right <= n - 1:
    if total == m:
        answer += 1
        right += 1
        if right <= n - 1:
            total += number[right]
        total -= number[left]
        left += 1
    elif total > m and right >= left + 1:
        total -= number[left]
        left += 1
    else:
        right += 1
        if right <= n - 1:
            total += number[right]

print(answer)
