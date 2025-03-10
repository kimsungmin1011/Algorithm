n, k = map(int, input().split())
hambuger = list(input())
people = []
count = 0

for i in range(n):
    if hambuger[i] == "P":
        people.append(i)

already_eat = set()

for i in people:
    flag = False
    for search in range(i - k, i + k + 1):
        if 0 <= search < n:
            if hambuger[search] == "H" and search not in already_eat:
                already_eat.add(search)
                flag = True
                break

    if flag == True:
        count += 1

print(count)
