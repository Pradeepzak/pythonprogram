n=int(input())
k=int(input())
l=[]
for i in range(1,n+1):
    l.append(i)
if(n>=k):
    b=l[:k]
    a=sum(b)
print(a)    
