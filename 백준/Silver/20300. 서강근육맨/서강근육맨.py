n = int(input())
machine = list(map(int, input().split()))
machine.sort()
answer = 0

left = 0
right = len(machine) - 1

if n % 2 == 0:
    while left <= right:
        number = machine[left] + machine[right]
        answer = max(answer, number)
        left += 1
        right -= 1
else:
    answer = machine[right]
    right -= 1
    while left <= right:
        number = machine[left] + machine[right]
        answer = max(answer, number)
        left += 1
        right -= 1

print(answer)
