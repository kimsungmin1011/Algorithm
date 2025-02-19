n, k = map(int, input().split())

yaksu = set()
for i in range(1, n + 1):
    if n % i == 0:
        yaksu.add(i)

if len(yaksu) >= k:
    print(sorted(yaksu)[k - 1])
else:
    print(0)
