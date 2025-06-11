from itertools import combinations

n = int(input())
people_list = [i for i in range(n)]

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

team_combi = list(combinations(people_list, n // 2))

min_score = int(1e9)

for i in range(len(team_combi)):
    team1 = team_combi[i]
    team1_combi = list(combinations(team1, 2))
    team1_score = 0
    for x, y in team1_combi:
        team1_score += graph[x][y]
        team1_score += graph[y][x]

    team2 = [i for i in range(n) if i not in team1]
    team2_combi = list(combinations(team2, 2))
    team2_score = 0
    for x, y in team2_combi:
        team2_score += graph[x][y]
        team2_score += graph[y][x]

    min_score = min(min_score, abs(team1_score - team2_score))

print(min_score)
