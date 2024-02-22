import sys
input=sys.stdin.readline

from collections import deque

def bfs(node1,node2):
    q=deque([node1])
    visited=[False for i in range(n)]
    #visited[node1]=True

    while True:
        if len(q)==0:
            break
        curNode=q.popleft()

        if curNode==node2:
            return True #같은 사이클에 있습니다
        for nextNode in updateIndexGraph[curNode]:
            if visited[nextNode]==True:
                continue
            visited[nextNode]=True
            q.append(nextNode)
        #print("q",q)
    return False


n,s,e,m=map(int,input().split())
graph=[]
for i in range(m):
    a,b,c=map(int,input().split())
    graph.append([a,b,c])

earn=list(map(int,input().split()))

updateGraph=[]
updateIndexGraph=[[]for i in range(n)]
for a,b,c in graph:
    updateGraph.append([a,b,c-earn[b]])
    updateIndexGraph[a].append(b)

print(updateGraph)
print(updateIndexGraph)

# 벨만포드
maxValue=10**10
dp=[maxValue for i in range(n)]
dp[s]=-earn[s]
ans=""
for i in range(n):
    for j in range(m):
        a,b,c=updateGraph[j]
        if dp[a]!=maxValue and dp[b]>dp[a]+c:
            dp[b]=dp[a]+c
            if i==n-1:
                print(a,e)
                if bfs(a,e): #만약 a랑e가 같은 사이클에 있다면
                    ans="Gee" #도착했을 때 돈을 무한히 많이 가지고 있을 수 있다
                    break

#이전 문제들에선 도착점이 고정되어 있지 않아서 dfs가 필요없었던 것.

if ans!="Gee":
    if dp[e]==maxValue:
        ans="gg"
    else:
        ans=-dp[e]

print(ans)