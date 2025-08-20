from itertools import permutations

n, k = map(int, input().split())
exercise = list(map(int, input().split()))
answer = 0

for i in permutations(exercise, n):
    weight = 500
    flag = True
    for j in i:
        weight -= k
        weight += j
        if weight < 500:
            flag = False
            break

    if flag == True:
        answer += 1

print(answer)
