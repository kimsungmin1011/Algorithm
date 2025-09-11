n = int(input())
m = int(input())
parent = [i for i in range(n)]


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x


for i in range(n):
    connect = list(map(int, input().split()))
    for j in range(n):
        if i != j and connect[j] == 1:
            if i < j:
                union(i, j)


flag = True
travel = list(map(int, input().split()))

for i in range(m - 1):
    first = find(travel[i] - 1)
    second = find(travel[i + 1] - 1)
    if first != second:
        flag = False
        break

if flag == True:
    print("YES")
else:
    print("NO")
