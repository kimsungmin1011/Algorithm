def solution(priorities, location):
    answer = 1
    visited = [False for _ in range(len(priorities))]

    while True:
        for i in range(len(priorities)):
            max_value = 0
            for i2 in range(len(priorities)):
                if visited[i2] == False:
                    max_value = max(max_value, priorities[i2])

            if visited[i] == False and priorities[i] == max_value:
                if i == location:
                    visited[i] = True
                    return answer

                visited[i] = True
                answer += 1
