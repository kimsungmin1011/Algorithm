n = int(input())

rope = []
for i in range(n):
    rope.append(int(input()))
rope.sort()

answer = 0

while n > 0:
    answer = max(answer, min(rope) * n)
    rope.pop(0)
    n -= 1

print(answer)
