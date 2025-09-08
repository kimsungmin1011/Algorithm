from collections import deque

alpha=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

def solution(begin, target, words):
    visited=set()
    visited.add(tuple(begin))
    
    def bfs():
        queue=deque([(begin, 0)])
        while queue:
            word,t=queue.popleft()
            if word == target:
                return t
            
            for i in range(len(list(begin))):
                nword=list(word)
                for j in range(len(alpha)):
                    nword[i]=alpha[j]
                    
                    if tuple(nword) not in visited and "".join(nword) in words:
                        visited.add(tuple(nword))
                        queue.append(("".join(nword), t + 1))
                        
        return 0
    
    answer=bfs()
    
    return answer