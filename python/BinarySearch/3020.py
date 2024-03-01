import sys
input=sys.stdin.readline

n,h=map(int,input().split())

ups=[0 for i in range(h+1)] #ups[i]는 i번째 칸에서 걸리는 상위 종유석 개수
downs=[0 for i in range(h+1)]
for i in range(n):
    length=int(input())
    if i%2==0:
        downs[length]+=1
    else:
        ups[h-length+1]+=1
#print(downs,ups)


accumDown=[0 for i in range(h+1)]
accumDown[-1]=downs[-1]
for i in range(h-1,0,-1):
    down=downs[i]
    accumDown[i]=accumDown[i+1]+down
#print(accumDown)

accumUp=[0 for i in range(h+1)]
accumUp[1]=ups[1]
for i in range(2,h+1):
    up=ups[i]
    accumUp[i]=accumUp[i-1]+up
#print(accumUp)

accumSum=[]
for i in range(h+1):
    accumSum.append(accumUp[i]+accumDown[i])
#print(accumSum)

minV=min(accumSum[1:])
count=accumSum[1:].count(minV)
print(minV,count)
