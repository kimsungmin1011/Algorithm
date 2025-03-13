n, m = map(int, input().split())
brand = []

for _ in range(m):
    brand.append(list(map(int, input().split())))

cost = int(1e9)
min_set = int(1e9)
min_each = int(1e9)

for i in brand:
    min_set = min(min_set, i[0])
    min_each = min(min_each, i[1])

if n >= 6:
    if min_set <= min_each * 6:
        cost = n // 6 * min_set
        n = n % 6
        if min_set <= n * min_each:
            cost += min_set
        else:
            cost += n * min_each
    else:
        cost = n * min_each

else:
    if min_set <= n * min_each:
        cost = min_set
    else:
        cost = n * min_each

print(cost)
