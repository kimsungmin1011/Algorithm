n, m = map(int, input().split())
trees = []

for _ in range(n):
    trees.append(int(input()))

start = 1
end = max(trees)
answer = 0

while start <= end:
    cut = (start + end) // 2
    count = 0

    for tree in trees:
        if tree >= cut:
            count += tree // cut

    if count >= m:
        answer = cut
        start = cut + 1
    else:
        end = cut - 1

print(answer)
