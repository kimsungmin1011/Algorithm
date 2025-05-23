n, m = map(int, input().split())
loc = list(map(int, input().split()))

plus = []
minus = []
for i in loc:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)

plus.sort(reverse=True)
minus.sort()

max_value = 0
for i in loc:
    if abs(i) > abs(max_value):
        max_value = i

result = abs(max_value)
for i in range(0, len(plus), m):
    if plus[i] != max_value:
        result += abs(plus[i] * 2)

for i in range(0, len(minus), m):
    if minus[i] != max_value:
        result += abs(minus[i] * 2)

print(result)
