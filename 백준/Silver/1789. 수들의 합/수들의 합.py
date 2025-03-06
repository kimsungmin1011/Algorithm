s = int(input())
answer = 0
count = 0

for i in range(1, s + 1):
    count += 1
    answer += i

    if answer > s:
        print(count - 1)
        break

    if answer == s:
        print(count)
        break
