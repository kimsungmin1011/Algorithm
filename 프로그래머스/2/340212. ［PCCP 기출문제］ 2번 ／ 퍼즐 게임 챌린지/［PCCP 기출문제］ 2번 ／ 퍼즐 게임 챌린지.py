def solution(diffs, times, limit):   
    start, end = 1, max(diffs)
    answer=0
    
    while start<=end:
        level = (start + end)//2
        current_time=0
        for i in range(len(diffs)):
            if diffs[i] <= level:
                current_time += times[i]
            else:
                if i > 0:
                    current_time += (times[i] + times[i-1]) * (diffs[i] - level) + times[i]
                else:
                    current_time += times[i] * (diffs[i] - level) + times[i]
    
        if current_time <= limit:
            answer = level
            end = level - 1
        else:
            start = level + 1
    
    return answer