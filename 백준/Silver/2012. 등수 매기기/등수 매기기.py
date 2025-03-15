import sys

input = sys.stdin.readline

N = int(input())

rank = []
for _ in range(N):
    rank.append(int(input()))
rank.sort()

cnt = 0

for i in range(N):
    if rank[i] != i + 1:  # 자기 예상 등수와 실제 등수가 다르면
        cnt += abs(rank[i] - (i + 1))  # 둘의 차이만큼 cnt에 더하기

print(cnt)
