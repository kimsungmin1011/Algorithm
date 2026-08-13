def solution(targets):
    answer = 0
    targets.sort(key=lambda x:(x[1],x[0]))
    last=targets[0][1]
    answer=1
    
    for i in range(1,len(targets)):
        if last<=targets[i][0]:
            last=targets[i][1]
            answer+=1
            
    return answer