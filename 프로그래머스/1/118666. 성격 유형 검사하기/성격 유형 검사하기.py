def solution(survey, choices):
    answer = ""
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0

    for i in range(len(choices)):
        c_survey = survey[i]
        if c_survey[0] == "R" or c_survey[0] == "T":
            if c_survey[0] == "R":
                score1 += choices[i] - 4
            else:
                score1 += 4 - choices[i]

        if c_survey[0] == "C" or c_survey[0] == "F":
            if c_survey[0] == "C":
                score2 += choices[i] - 4
            else:
                score2 += 4 - choices[i]

        if c_survey[0] == "J" or c_survey[0] == "M":
            if c_survey[0] == "J":
                score3 += choices[i] - 4
            else:
                score3 += 4 - choices[i]

        if c_survey[0] == "A" or c_survey[0] == "N":
            if c_survey[0] == "A":
                score4 += choices[i] - 4
            else:
                score4 += 4 - choices[i]

    if score1 <= 0:
        answer += "R"
    elif score1 > 0:
        answer += "T"

    if score2 <= 0:
        answer += "C"
    else:
        answer += "F"

    if score3 <= 0:
        answer += "J"
    else:
        answer += "M"

    if score4 <= 0:
        answer += "A"
    else:
        answer += "N"

    return answer
