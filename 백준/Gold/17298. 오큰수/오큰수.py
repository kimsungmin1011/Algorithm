import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

answer = [-1] * n
stack = []

for i in range(n):
    # 현재 수가 stack의 top 인덱스에 해당하는 값보다 크면 오큰수!
    while stack and a[stack[-1]] < a[i]:
        idx = stack.pop()
        answer[idx] = a[i]
    stack.append(i)

print(*answer)
