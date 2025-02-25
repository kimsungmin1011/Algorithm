from collections import deque

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))  # i번 건물 한 개를 짓기 위해서 걸리는 시간

    indegree = [0] * n  # i번 건물의 선행 건물 개수 (진입 차수)
    dp = [0] * n  # i번 건물을 짓기 위해서 걸리는 누적 시간

    graph = [[] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        indegree[b - 1] += 1  # 진입 차수 계산
        graph[a - 1].append(b - 1)  # 각 건물별 선행 관계 (a를 짓고난 후 b를 지음)

    w = int(input())  # 목표 건물 번호
    w -= 1

    queue = deque()  # 위상정렬 구현 위한 큐

    # 진입 차수 0인 건물 큐에 삽입
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    # 진입 차수 0인 건물부터 순서대로 탐색
    while queue:
        current = queue.popleft()
        dp[current] += d[current]  # 현재 건물 건설 시간 더해줌

        for next in graph[current]:
            indegree[next] -= 1
            # max를 쓰는 이유: 가장 오래 걸리는 선행 건물이 완공돼야 다음 건물 건설 가능
            dp[next] = max(dp[next], dp[current])

            if indegree[next] == 0:
                # 만약 다음 건물의 진입 차수가 0이 됐다면 큐에 삽입 (선행 건물 다 지어짐)
                queue.append(next)

    print(dp[w])
