import heapq

n = int(input())
lesson = []

for _ in range(n):
    lesson.append(list(map(int, input().split())))

lesson.sort(key=lambda x: x[1])

room = [lesson[0][2]]
max_room = 1
r_count = 1

for i in range(1, len(lesson)):
    if room[0] <= lesson[i][1]:
        heapq.heappop(room)
        heapq.heappush(room, lesson[i][2])
    else:
        heapq.heappush(room, lesson[i][2])
        r_count += 1
        max_room = max(max_room, r_count)

print(max_room)
