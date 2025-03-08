import sys

input = sys.stdin.readline

N = int(input())

timeline = []
for i in range(N):
    start, end = map(int, input().split())
    timeline.append((start, end))

timeline.sort(key=lambda x: (x[1], x[0]))
count = 0
end = 0

for i in range(N):
    if timeline[i][0] >= end:
        end = timeline[i][1]
        count += 1

print(count)
