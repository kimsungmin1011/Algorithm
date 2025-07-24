def solution(record):
    answer = []
    user_id = {}

    for i in record:
        i = i.split(" ")
        if i[0] == "Enter" or i[0] == "Change":
            user_id[i[1]] = i[2]

    for i in record:
        i = i.split(" ")
        if i[0] == "Enter":
            answer.append(user_id[i[1]] + "님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(user_id[i[1]] + "님이 나갔습니다.")

    return answer
