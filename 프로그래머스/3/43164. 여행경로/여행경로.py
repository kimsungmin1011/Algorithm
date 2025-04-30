def solution(tickets):
    course = {}  # 출발지 → 도착지 리스트
    visited = {}  # 출발지 → 도착지별 방문 여부 (항공권 기준!)

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
                    visited[current][next] = True        # 항공권 사용 체크
                    route.append(next_airport)           # 경로에 추가
                    dfs(next_airport)                    # 다음 공항 탐색
                    visited[current][next] = False       # 항공권 사용 복구
                    route.pop()                          # 경로 복구

        # 모든 항공권을 사용했는지 확인
        flag = True
        for i in visited:
            if False in visited[i]:                      # 하나라도 안 쓴 항공권이 있다면
                flag = False
                break

        if flag == True:
            total_route.append(route[:])                 # 완성된 경로 저장

    dfs("ICN")

    return sorted(total_route)[0]                        # 사전순 가장 앞선 경로 반환
