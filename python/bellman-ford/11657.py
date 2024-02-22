import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for i in range(m):
    a,b,c=map(int,input().split())
    graph.append([a,b,c])

#print(graph)


#벨만포드
maxValue=sys.maxsize
dp=[maxValue for i in range(n+1)]
start=1
dp[start]=0
cycle=False
for i in range(1,n+1): #1~n-1까지 최대 n-1개의 간선 연결, 마지막 추가 1번은 사이클 발생하는지 탐지
    for j in range(m): #m개의 모든 간선에 대해 업데이트 가능한지 확인
        a,b,c=graph[j]
        #⭐️ dp[a]!=maxValue 체크해야 하는 이유
        #   : dp[start]=0으로 시작점만 도달 가능하게 체크해줬다.
        #   : 만약 dp[a(현재 탐색의 출발점)]이 maxValue라면, start를 거쳐서 여기에 도달하지 못했다는 뜻
        #   : 그런 상태에서 a->b를 탐색하면, start없이 a->b를 계산하게 되는건데, 우리가 구하는 start에서의 최소 경로가 아니게 된다.
        #   : 1이 출발 지점이고 2<->3의 경로가 있다면, 2<->3 사이클을 감지하게 되는데, 애초에 1은 2나 3으로 갈 수 없으므로 2<->3 경로는 탐지하면 안되는 것이다.
        #   : 3 2   2 3 -1  3 2 1
        if dp[a]!=maxValue and dp[b]>dp[a]+c:
            dp[b]=dp[a]+c
            if i==n:
                cycle=True
                break # ⭐️ 빠른 탐색을 위해 break걸어줄 것
    if cycle: # 뭐 크게 차이는 안나는데
        break
#print(cycle,dp)

ans=[]
if cycle:
    ans.append(-1)
else:
    for i in range(2,n+1):
        if dp[i]!=maxValue: # ⭐️ 사이클이 없더라도 갈 수 있는 곳은 있을 수 있다!!!
            ans.append(dp[i])
        else:
            ans.append(-1)

for i in ans:
    print(i)