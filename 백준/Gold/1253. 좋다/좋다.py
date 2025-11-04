n = int(input())
number = list(map(int, input().split()))
number.sort()
answer = 0

for i in range(n):
    start = 0 if i != 0 else 1
    end = n - 1 if i != n - 1 else n - 2

    while start < end:
        current = number[start] + number[end]
        if current > number[i]:
            if end - 1 != i:
                end -= 1
            else:
                end -= 2
        elif current < number[i]:
            if start + 1 != i:
                start += 1
            else:
                start += 2
        else:
            answer += 1
            break

print(answer)
