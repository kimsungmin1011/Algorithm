n = int(input())
number = list(map(int, input().split()))
number.sort()

left, right = 0, n - 1
answer_v = int(1e11)
answer_x, answer_y = 0, n - 1

while left < right:
    current = number[left] + number[right]
    if answer_v > abs(current):
        answer_v = abs(current)
        answer_x, answer_y = number[left], number[right]

    if current > 0:
        right -= 1
    else:
        left += 1

print(answer_x, answer_y)
