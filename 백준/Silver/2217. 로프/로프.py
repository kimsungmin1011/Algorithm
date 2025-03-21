n = int(input())
roaf = []
for _ in range(n):
    roaf.append(int(input()))

roaf.sort(reverse=True)
max_roaf = 0
min_weight = int(1e9)

for i in range(n):
    min_weight = min(min_weight, roaf[i])
    max_roaf = max(max_roaf, min_weight * (i + 1))

print(max_roaf)
