import sys
from collections import deque

input = sys.stdin.read
data = input().split("\n")

n = int(data[0])

# 건물 정보 저장 (1-indexed)
building = [[] for _ in range(n + 1)]
time = [0] * (n + 1)  # 각 건물을 짓는 데 걸리는 기본 시간

# indegree는 현재 건물을 짓기 위해 필요한 선행 건물의 총 개수
indegree = [0] * (n + 1)  # 진입 차수

graph = [[] for _ in range(n + 1)]  # 건물 간 의존 관계를 나타내는 그래프
dp = [0] * (n + 1)  # 각 건물 완성까지 걸리는 '누적' 최소 시간

# 입력 파싱 및 그래프 구성
for i in range(1, n + 1):
    line = list(map(int, data[i].split()))
    time[i] = line[0]  # 건물을 짓는 데 걸리는 시간
    for j in range(1, len(line) - 1):  # line의 마지막 -1은 종료 표식
        pre_building = line[j]
        graph[pre_building].append(i)
        indegree[i] += 1

# 위상 정렬(BFS)에 사용할 큐
queue = deque()

# 1. 진입 차수(indegree)가 0인 건물(즉, 먼저 지어야 하는 건물이 없는 건물)을 큐에 삽입
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]  # 선행 건물이 없는 건물은 자기 건설 시간 그대로 dp에 저장

# 2. 큐에서 원소를 꺼내며(=현재 건물), 그 건물과 연결된(=의존하는) 건물들의 진입 차수를 업데이트
while queue:
    now = queue.popleft()  # 큐에서 현재 건물을 꺼낸다

    # 현재 건물을 선행 건물로 하는 모든 건물(next_building)에 대해
    for next_building in graph[now]:
        # now 건물 완성 후 next_building을 지을 수 있으므로, next_building의 진입 차수 감소
        indegree[next_building] -= 1

        # next_building의 최소 건설 시간은
        #   '현재까지 dp[now](now 건물 완성에 걸린 시간) + next_building 자체 건설 시간' 중 최댓값
        dp[next_building] = max(dp[next_building], dp[now] + time[next_building])

        # 새로 진입 차수가 0이 된 건물은 모든 선행 건물이 완성되었으므로 큐에 삽입
        if indegree[next_building] == 0:
            queue.append(next_building)

# 3. 모든 건물에 대한 최소 건설 시간 출력
for i in range(1, n + 1):
    print(dp[i])
