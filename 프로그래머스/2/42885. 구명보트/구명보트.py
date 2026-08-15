def solution(people, limit):
    answer = 0
    people.sort()
    n=len(people)
    visited=[False for _ in range(n)]
    last=n-1
    
    for i in range(n):
        if visited[i]==True:
            continue
        light=people[i]
        answer+=1
        
        if light>limit/2:
            continue
            
        for j in range(last,i,-1):
            heavy=people[j]
            if light+heavy<=limit:
                visited[j]=True
                last=j-1
                # print(light,heavy)
                break
                
    return answer