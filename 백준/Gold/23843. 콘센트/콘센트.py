import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tasks = list(map(int, input().split()))

# 작업 수 ≤ 서버 수라면, 최장 작업 시간만 걸린다
if m >= n:
    print(max(tasks))
    sys.exit()

# 1) m개의 서버 초기화
server_loads = [0] * m
heapq.heapify(server_loads)

# 2) 가장 긴 작업부터 차례로 할당
for t in sorted(tasks, reverse=True):
    cur = heapq.heappop(server_loads)  # 부하가 최소인 서버를 선택
    # → 이 서버는 지금까지 'cur' 시간만큼 일했고, 여기서 새 작업 't'를 더 하게 됨
    heapq.heappush(server_loads, cur + t)  # 증가된 부하(cur + t)를 힙에 다시 저장

# 3) 전체 완료 시간 = 가장 무거운 서버 부하
print(max(server_loads))
