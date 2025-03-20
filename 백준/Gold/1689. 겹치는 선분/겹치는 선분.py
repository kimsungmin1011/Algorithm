import sys

n = int(sys.stdin.readline().strip())
events = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    events.append((start, 1))  # 선분 시작
    events.append((end, -1))  # 선분 종료

# 정렬
events.sort()

max_overlap = 0
current_overlap = 0

# 스위핑 진행
for _, event in events:
    current_overlap += event
    max_overlap = max(max_overlap, current_overlap)

print(max_overlap)
