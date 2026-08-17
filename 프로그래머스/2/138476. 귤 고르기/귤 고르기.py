from collections import Counter

def solution(k, tangerine):
    c_tangerine=Counter(tangerine)
    answer=len(c_tangerine)
    total=sum(c_tangerine.values())
    c_tangerine=[[i,c_tangerine[i]] for i in c_tangerine]
    c_tangerine.sort(key= lambda x: x[1])
    
    # 매 턴마다 
    for ke,v in c_tangerine:
        #현재 뽑는 크기의 귤의 개수가 최소이면서 이걸 뽑았을 때 남아있는 귤이 k개 이상이라면
        if total-v>=k:
            total-=v
            answer-=1
            
    return answer