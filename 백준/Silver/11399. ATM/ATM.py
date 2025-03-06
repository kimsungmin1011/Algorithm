n = int(input())

p = list(map(int, input().split()))
p.sort()

answer = 0
for i in range(n + 1):
    answer += sum(p[:i])

print(answer)
