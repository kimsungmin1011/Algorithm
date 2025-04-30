def solution(tickets):
    course = {}
    visited = {}

    for i, j in tickets:
        if i not in course:
            course[i] = [j]
            visited[i] = [False]
        else:
            course[i].append(j)
            visited[i].append(False)

    total_route = []
    route = ["ICN"]

    def dfs(current):
        if current in course:
            for next in range(len(course[current])):
                next_airport = course[current][next]
                if visited[current][next] == False:
                    visited[current][next] = True
                    route.append(next_airport)
                    dfs(next_airport)
                    visited[current][next] = False
                    route.pop()

        flag = True
        for i in visited:
            if False in visited[i]:
                flag = False
                break

        if flag == True:
            total_route.append(route[:])

    dfs("ICN")

    return sorted(total_route)[0]
