import sys

input = sys.stdin.readline

N = int(input())

timeline = []
for i in range(N):
    start, end = map(int, input().split())
    timeline.append((end, start))

timeline.sort()
count = 0
end = 0

for i in range(N):
    if timeline[i][1] >= end:
        end = timeline[i][0]
        count += 1

print(count)
