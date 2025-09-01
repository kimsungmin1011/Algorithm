def solution(N, stages):
    answer = []
    
    current=len(stages)
    for stage in range(1,N+1):
        count=0
        for i in stages:
            if i==stage:
                count+=1
        if count>0:
            answer.append((count/current, -stage))
            current-=count
        else:
            answer.append((0,- stage))
    
    answer.sort(reverse=True)
    final=[-i[1] for i in answer]
    return final