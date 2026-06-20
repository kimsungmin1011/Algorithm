from collections import deque

def solution(x, y, n):
    answer = 0
    queue=deque([(x,0)])
    visited=set()
    visited.add(x)
    
    while queue:
        node,time=queue.popleft()
        if node==y:
            return time
        
        n1,n2,n3=node+n,node*2,node*3
        for nx in [n1,n2,n3]:
            if nx<=y and nx not in visited:
                visited.add(nx)
                queue.append((nx,time+1))
                
    return -1