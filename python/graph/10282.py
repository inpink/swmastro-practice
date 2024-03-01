import sys
input=sys.stdin.readline

import heapq

t=int(input())
for i in range(t):
    n,d,c=map(int,input().split())
    graph=[[]for i in range(n+1)]
    for j in range(d):
        a,b,s=map(int,input().split()) #a<-b   s
        graph[b].append((a,s)) #b->a  s

    #다익스트라
    heap=[]
    start=c #시작점 : 해킹당한 컴퓨터
    count=0
    countTime=0
    heapq.heappush(heap,(start,0)) #누적time,현재노드,누적count
    maxValue=10**10
    dp=[[maxValue,-1] for i in range(n+1)]
    dp[start][0]=0
    while True:
        if len(heap)==0:
            break

        curNode,curCount=heapq.heappop(heap)

        for nextNode,nextTime in graph[curNode]:
            if dp[nextNode][0]>dp[curNode][0]+nextTime:
                dp[nextNode]=(dp[curNode][0]+nextTime,count+1)
                heapq.heappush(heap,[nextNode,count+1])
    #print(dp)

    maxTime=0
    maxCount=0
    for i in range(1,n+1):
        if dp[i][0]==maxValue:
            continue
        else:
            maxCount+=1
            maxTime=max(maxTime,dp[i][0])
    print(maxCount, maxTime)
'''
여기서
다익스트라 vs dfs/bfs 차이점
일반적인 dfs/bfs는 각 간선의 가중치가 평등해야 한다!
여기서는 간선을 적게 건너는게 아니라 간선을 100만개 건너더라도 cost가 작은 것이 우선이니까
=> 다익스트라

'''