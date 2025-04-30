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

    final_answer = []
    route = ["ICN"]

    def dfs(current):
        if current in course:
            for next in range(len(course[current])):
                if visited[current][next] == False:
                    visited[current][next] = True
                    route.append(course[current][next])
                    dfs(course[current][next])
                    visited[current][next] = False
                    route.pop()

        flag = True
        for next in visited:
            if False in visited[next]:
                flag = False
                break

        if flag == True:
            final_answer.append(route[:])

    dfs("ICN")

    return sorted(final_answer)[0]