n, m = map(int, input().split())

parent = [i for i in range(n)]
danger = list(map(int, input().split()))
danger.pop(0)
danger = [i - 1 for i in danger]


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a in danger and b in danger:
        return
    elif a in danger:
        parent[b] = a
    elif b in danger:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


all_party = []

for _ in range(m):
    party = list(map(int, input().split()))
    len_number = party.pop(0)
    all_party.append(party)
    for j in range(len_number - 1):
        union(party[j] - 1, party[j + 1] - 1)

answer = 0
for i in range(m):
    if all(find(j - 1) not in danger for j in all_party[i]):
        answer += 1

print(answer)
