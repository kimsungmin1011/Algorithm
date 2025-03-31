line = list(input())
stack = []
count = 0

for i in range(len(line)):
    if line[i] == "(":
        stack.append("(")
    else:
        if stack and stack[-1] == "(":
            if i > 0 and line[i - 1] == "(":
                count += len(stack) - 1
            else:
                count += 1
            stack.pop()

print(count)
