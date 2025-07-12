def solution(new_id):
    answer = ""
    new_list = []

    for i in new_id:
        if 65 <= ord(i) <= 90:
            i = chr(ord(i) + 32)
            new_list.append(i)
        elif (
            97 <= ord(i) <= 122
            or i == "-"
            or i == "_"
            or i == "."
            or 48 <= ord(i) <= 57
        ):
            new_list.append(i)

    new_id = new_list[:]
    new_list = [new_id[0]]

    for i in range(1, len(new_id)):
        if new_id[i] == "." and new_id[i - 1] == ".":
            continue
        else:
            new_list.append(new_id[i])

    new_id = new_list[:]
    new_list = []

    for i in range(len(new_id)):
        if (i == 0 or i == len(new_id) - 1) and new_id[i] == ".":
            continue
        else:
            new_list.append(new_id[i])

    new_id = new_list[:]
    new_list = []

    if len(new_id) == 0:
        new_id.append("a")

    for i in range(len(new_id)):
        if i >= 15:
            continue
        else:
            new_list.append(new_id[i])

    new_id = new_list[:]

    if new_id[-1] == ".":
        new_id.pop()

    while len(new_id) < 3:
        new_id.append(new_id[-1])

    answer = "".join(new_id)
    return answer
