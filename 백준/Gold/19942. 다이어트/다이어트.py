n = int(input())

mp, mf, ms, mv = map(int, input().split())
foods = []

for i in range(n):
    foods.append(list(map(int, input().split())))

min_cost = int(1e9)
ingredients = []
min_ingredients = []


def dfs(idx, p, f, s, v, cost):
    global min_cost, min_ingredients
    if p >= mp and f >= mf and s >= ms and v >= mv:
        if min_cost > cost:
            min_ingredients = [ingredients[:]]
            min_cost = cost
        elif min_cost == cost:
            min_ingredients.append(ingredients[:])
        return

    for i in range(idx, n):
        ingredients.append(i + 1)
        dfs(
            i + 1,
            p + foods[i][0],
            f + foods[i][1],
            s + foods[i][2],
            v + foods[i][3],
            cost + foods[i][4],
        )
        ingredients.pop()


dfs(0, 0, 0, 0, 0, 0)

if min_cost != int(1e9):
    print(min_cost)
    print(*sorted(min_ingredients)[0])
else:
    print(-1)
