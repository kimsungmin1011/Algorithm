import sys

input = sys.stdin.readline

array = list(input().strip())

answer = 0
flag = True
counta = 0
countb = 0
stack = [array[0]]

if array[0] == "(":
    counta = 1
elif array[0] == "[":
    countb = 1
else:
    print(0)
    exit()

for i in range(1, len(array)):
    if array[i] == "]":
        if stack and stack[-1] == "[":
            stack.pop()
            countb -= 1
            if array[i - 1] == "[":
                answer += 2**counta * 3**countb * 3
        else:
            flag = False
            break

    elif array[i] == ")":
        if stack and stack[-1] == "(":
            stack.pop()
            counta -= 1
            if array[i - 1] == "(":
                answer += 2**counta * 3**countb * 2
        else:
            flag = False
            break

    elif array[i] == "[":
        countb += 1
        stack.append("[")

    elif array[i] == "(":
        counta += 1
        stack.append("(")

if len(stack) == 0 and counta == 0 and countb == 0 and flag == True:
    print(answer)
else:
    print(0)
