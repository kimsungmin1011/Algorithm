t = int(input())


def find(x, parent):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x], parent)
        return parent[x]


def union(x, y, parent):
    a = find(x, parent)
    b = find(y, parent)
    if a != b:
        parent[b] = a


for i in range(t):
    n = int(input())
    parent = [i for i in range(n)]

    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b, parent)

    m = int(input())
    answer = []
    for _ in range(m):
        u, v = map(int, input().split())
        a = find(u, parent)
        b = find(v, parent)
        if a != b:
            answer.append(0)
        else:
            answer.append(1)

    print(f"Scenario {i+1}:")
    for a in answer:
        print(a)
    print("")
