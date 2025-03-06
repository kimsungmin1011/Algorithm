n=int(input())

stack=list(map(int,input().split()))
hap=0
stack1=[]

for i in sorted(stack):
    stack1.append(i)
    hap+=sum(stack1)
    
print(hap)