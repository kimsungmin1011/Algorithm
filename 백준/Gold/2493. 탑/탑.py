n = int(input())
tower = list(map(int, input().split()))
stack = []
height = [0 for _ in range(n)]

for i in range(n):
    while stack and tower[stack[-1]] <= tower[i]:
        stack.pop()
    if stack:
        height[i] = stack[-1] + 1
    stack.append(i)

print(*height)
