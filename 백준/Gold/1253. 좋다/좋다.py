n = int(input())
number = list(map(int, input().split()))
number.sort()
answer = 0

for i in range(n):
    start = 0
    end = n - 1
    while start < end:
        if start == i:
            start += 1
            continue
        elif end == i:
            end -= 1
            continue

        current = number[start] + number[end]
        if current > number[i]:
            end -= 1
        elif current < number[i]:
            start += 1
        else:
            answer += 1
            break

print(answer)
