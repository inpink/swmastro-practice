import sys
input=sys.stdin.readline

tc=int(input())
for i in range(tc):
    n,m,w=map(int,input().split())

    graph=[]
    for j in range(m):
        s,e,t=map(int,input().split())
        graph.append([s,e,t])
        graph.append([e,s,t])
    for j in range(w):
        s,e,t=map(int,input().split())
        graph.append([s,e,-t])
    #print(graph)

    #벨만포드
    maxValue=sys.maxsize
    dp=[maxValue for i in range(n+1)]
    start=1 # ⭐️ 벨만포드에서 사이클이 있는 지만을 판단하는 것은 시작점이 어디든 상관없다
    dp[start]=0
    cycle=False
    for i in range(1,n+1):
        for j in range(m*2+w):
            # ⭐️ 대신 일반적인 벨만포드와 다르게 시작점을 거치지 않더라도 검사해줘야 한다.
            # 따라서 이 방식으론 사이클이 없을 때 시작점에서의 각 노드까지의 최소 비용을 구하긴 어렵다
            s,e,t=graph[j]
            if dp[e]>dp[s]+t:
                dp[e]=dp[s]+t
                if i==n:
                   cycle=True
                   break
    #print(dp)
    if cycle:
        print("YES")
    else:
        print("NO")