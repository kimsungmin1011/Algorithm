from collections import Counter

def solution(topping):
    answer = 0
    ldict=dict()
    rdict=Counter(topping)
    
    for i in topping:
        if i not in ldict:
            ldict[i]=1
        else:
            ldict[i]+=1
        rdict[i]-=1
        if rdict[i]==0:
            del rdict[i]
        
        if len(ldict)==len(rdict):
            answer+=1
        
    return answer