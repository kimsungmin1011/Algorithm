import heapq

n, m = map(int, input().split())

box = list(map(int, input().split()))  # 각 상자별 장난감 개수
box_q = []  # 학생들이 원하는 장난감 개수
for i in box:
    heapq.heappush(box_q, -i)

want = list(map(int, input().split()))

flag = True

for currnet in want:
    if box_q:
        out = heapq.heappop(box_q)
        if currnet < -out:
            heapq.heappush(box_q, -(-out - currnet))
        elif currnet > -out:
            flag = False
            break
    else:
        flag = False
        break

if flag == True:
    print(1)
else:
    print(0)
