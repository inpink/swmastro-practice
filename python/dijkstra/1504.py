import sys
input=sys.stdin.readline
import heapq

def dijk(start,n):
    maxValue=sys.maxsize
    dp=[maxValue for i in range(n+1)]

    heap=[]
    heapq.heappush(heap,(0,start))
    while True:
        if len(heap)==0:
            break
        cost,node=heapq.heappop(heap)
        for nextNode,nextCost in graph[node]:
            newCost=nextCost+cost

            if (dp[nextNode]>newCost):
                dp[nextNode]=newCost
                heapq.heappush(heap,(newCost,nextNode))
        #print("heap",heap)

    dp[start]=0
    return dp

maxValue=sys.maxsize
n,e=map(int,input().split())
graph=[ [] for i in range(n+1)]
for i in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

inter1,inter2=map(int,input().split())

#for i in graph:
    #print(i)


#다익스트라
#1->inter1->inter2->n
#1->inter2->inter1->n

startOne =dijk(1,n)
startInter1 = dijk(inter1,n)
startInter2 = dijk(inter2,n)
#print(startOne)
#print(startInter1)
#print(startInter2)


oneToInter1Value= startOne[inter1]
oneToInter2Value= startOne[inter2]
inter1ToInter2Value = startInter1[inter2]
inter2ToInter1Value = startInter2[inter1]
inter1toEndValue = startInter1[n]
inter2toEndValue = startInter2[n]

ansList=[]
if (oneToInter1Value!=maxValue
        and inter1ToInter2Value!=maxValue
        and inter2toEndValue!=maxValue):
    ansList.append(oneToInter1Value+inter1ToInter2Value+inter2toEndValue)

if (oneToInter2Value!=maxValue
        and inter2ToInter1Value!=maxValue
        and inter1toEndValue!=maxValue):
    ansList.append(oneToInter2Value+inter2ToInter1Value+inter1toEndValue)

if len(ansList)==0:
    ans=-1
else:
    ans=min(ansList)

print(ans)