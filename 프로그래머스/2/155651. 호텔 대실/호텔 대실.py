import heapq

def solution(book_time):
    answer = 0
    n_book_time=[]
    
    for s,e in book_time:
        sh,sm=s.split(':')
        st=int(sh)*60+int(sm)
        eh,em=e.split(':')
        et=int(eh)*60+int(em)
        
        n_book_time.append((st,et))
    
    n_book_time.sort()
    
    room=[n_book_time[0][1]]
    count=1
    
    for i in range(1,len(book_time)):
        if n_book_time[i][0]>=room[0]+10:
            heapq.heappop(room)
            heapq.heappush(room,n_book_time[i][1])
        else:
            count+=1
            heapq.heappush(room,n_book_time[i][1])
    
    return count
        
    return answer