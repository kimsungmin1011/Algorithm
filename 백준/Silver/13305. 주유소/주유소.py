n = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))

min_oil = int(1e9)
cost = 0

for i in range(n - 1):
    min_oil = min(min_oil, oil[i])
    cost += min_oil * distance[i]

print(cost)
