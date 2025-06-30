n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
final_cut = 0

while start <= end:
    cut = (start + end) // 2
    count = 0

    for tree in trees:
        if tree >= cut:
            count += tree - cut

    if cut > final_cut and count >= m:
        final_cut = cut
        start = cut + 1
    else:
        end = cut - 1

print(final_cut)
