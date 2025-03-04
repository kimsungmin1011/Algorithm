import sys

input = sys.stdin.readline

stack = []
answer = []

n = int(input())
index = 1

for _ in range(n):
    number = int(input())

    while number >= index:
        stack.append(index)
        index += 1
        answer.append("+")

    if len(stack) > 0 and number == stack[-1]:
        stack.pop()
        answer.append("-")

    else:
        print("NO")
        exit()

for i in answer:
    print(i)
