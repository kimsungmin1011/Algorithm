import sys

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n)]
parents = list(map(int, input().split()))
kill = int(input())
start = []

for i in range(len(parents)):
    if parents[i] == -1:
        start.append(i)
        continue
    tree[parents[i]].append(i)

visited = [False for _ in range(n)]
leaf_count = 0


def dfs(node):
    global leaf_count
    flag = False

    if node == kill:
        return

    for i in tree[node]:
        if i == kill:
            continue

        if visited[i] == False:
            flag = True
            visited[i] = True
            dfs(i)

    if flag == False:
        leaf_count += 1
        return


for i in start:
    dfs(i)
    visited[i] = True

print(leaf_count)
