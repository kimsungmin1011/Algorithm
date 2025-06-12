import heapq

# 인구수, 센티 키, 사용 횟수 제한
n, h, t = map(int, input().split())

height = []
for _ in range(n):
    heapq.heappush(height, -int(input()))

time = 0

for i in range(t):
    if -height[0] >= h:
        if -height[0] != 1:
            out = heapq.heappop(height)
            heapq.heappush(height, -(-out // 2))
        time += 1
    else:
        break

if -height[0] >= h:
    print("NO")
    print(-height[0])
else:
    print("YES")
    print(time)
