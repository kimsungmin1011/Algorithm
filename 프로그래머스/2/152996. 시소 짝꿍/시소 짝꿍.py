from collections import Counter

def solution(weights):
    answer = 0
    weights=Counter(weights)
    
    for i in weights:
        if weights[i]>1:
            answer+=(weights[i])*(weights[i]-1)//2
            
        if i*1.5 in weights:
            answer+=weights[i]*weights[i*1.5]
            
        if i*2 in weights:
            answer+=weights[i]*weights[i*2]
            
        if i*4/3 in weights:
            answer+=weights[i]*weights[i*4/3]
    
    return answer