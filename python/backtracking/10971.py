import sys
input=sys.stdin.readline

minV=10**10
def dfs(graph,visited,n,root,start,end,cost,count):
    global minV
    #print(visited,root,start,end,cost,count)

    if count==n:
        if graph[end][root]!=0:
            cost+=graph[end][root]
            minV=min(minV,cost)
            #print(minV)
        return

    for i in range(n):
        if visited[i]:
            continue
        if graph[end][i]==0:
            continue
        newCost=cost+graph[end][i]
        visited[i]=True
        dfs(graph,visited,n,root,end,i,newCost,count+1)
        visited[i]=False

def solution():
    n=int(input())

    graph=[]
    for i in range(n):
        row=list(map(int,input().split()))
        graph.append(row)

    visited=[False for i in range(n)]
    for i in range(n):
        visited[i]=True
        dfs(graph,visited,n,i,0,i,0,1)
        visited[i]=False

    print(minV)

solution()
'''
이 문제
브루트 포스로 해도 풀리지만
0123456789과 0123456798는 3개밖에 차이안난다
10개를 매번 새롭게 해주는 시간보다
⭐️⭐️ "백트래킹"으로 바뀌지 않은 부분 연산을 최소화하는 것이 더 효율적이다 ⭐️⭐️
visited는 하나만 써도 괜찮다!!!! 어차피 min값 연산하는 건 동시에 일어나지 않기 때문!!!
다음 min연산을 할때는 이미 백트래킹으로 visited[x]=False이 되어있을거기 떄문!!

'''