while True:

    word = input()

    stack = []
    balance = True

    if word == ".":
        break

    for i in word:
        if i == "(" or i == "[":
            stack.append(i)

        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                balance = False
                break

        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                balance = False
                break

    if balance == True and len(stack) == 0:
        print("yes")
    else:
        print("no")
