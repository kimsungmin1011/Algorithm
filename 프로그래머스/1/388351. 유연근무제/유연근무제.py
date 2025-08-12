def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        cut = schedules[i]
        cut_m = cut // 100 * 60 + cut % 100
        cut_m += 10

        flag = True
        count = startday
        for j in range(7):
            if count == 6 or count == 7 or count == 13:
                count += 1
                continue
            count += 1
            c_time = timelogs[i][j]
            c_time_m = c_time // 100 * 60 + c_time % 100

            if c_time_m > cut_m:
                flag = False
                break

        if flag == True:
            answer += 1

    return answer
