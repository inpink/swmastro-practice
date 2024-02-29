import sys
input=sys.stdin.readline

n,k=map(int,input().split())
sRoot=int(n**0.5)
#print(sRoot)

ansSet=set()
for i in range(1,sRoot+1):
    if n%i==0:
        ansSet.add(i)
        ansSet.add(n//i)
ansList=list(ansSet)
ansList.sort()
#print(ansList)
if len(ansList)<k:
    print(0)
else:
    print(ansList[k-1])