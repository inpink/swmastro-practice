import sys
input=sys.stdin.readline

n=int(input())
features=list(map(int,input().split()))
features.sort()
#print(features)

#binary search
start=0
end=n-1
ansSum=2_000_000_000+1
answer=[]
while True:
    if start==end:
        break

    sumValue=features[start]+features[end]
    if sumValue==0:
        ansSum=0
        answer=[features[start],features[end]]
        break

    if abs(sumValue)<ansSum:
        ansSum=abs(sumValue)
        answer=[features[start],features[end]]

    if sumValue>0:
        end-=1
    elif sumValue<0:
        start+=1
    #print(start,end)
answer.sort()
print(*answer)