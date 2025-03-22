def solution(n, lost, reserve):
    answer = n - len(lost)
    lost = set(lost)
    reserve.sort()
    remove_list = set()
    
    for i in reserve:
        if i in lost:
            answer += 1
            lost.remove(i)
            remove_list.add(i)
    
    for i in remove_list:
        reserve.remove(i)
        
    for i in reserve:
        if i - 1 in lost:
            answer += 1
            lost.remove(i - 1)
    
        elif i + 1 in lost:
            answer += 1
            lost.remove(i + 1)
    
    return answer