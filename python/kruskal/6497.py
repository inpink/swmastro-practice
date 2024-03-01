import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
import heapq
def find(vRoot,x):
    if vRoot[x]!=x:
        vRoot[x]=find(vRoot,vRoot[x])
    return vRoot[x]

def solution():
    while True:
        n,m=map(int,input().split())
        if n==0 and m==0:
            exit(0)
        graph=[[]for i in range(n)]
        heap=[]
        vRoot=[i for i in range(n)]
        totalCost=0
        for i in range(m):
            a,b,c=map(int,input().split())
            graph[a]=((b,c))
            graph[b]=((a,c))
            heapq.heappush(heap,(c,a,b))
            totalCost+=c

        connect=0
        connectCount=0
        while True:
            if len(heap)==0:
                break

            if connectCount==n-1:
                break

            cost,nodeA,nodeB=heapq.heappop(heap)
            parentA=find(vRoot,nodeA)
            parentB=find(vRoot,nodeB)

            if parentA==parentB:
                continue
            else:
                vRoot[parentB]=parentA #A<-B 편입시킴
                connect+=cost
                connectCount+=1
                #print(nodeA,nodeB)
        #print(connect,connectCount)
        print(totalCost-connect)
solution()