import sys
input=sys.stdin.readline

def dfs(start,count):
    if count==5:
        print(1)
        exit(0)

    for nextNode in graph[start]:
        if visited[nextNode]==False:
            visited[nextNode]=True
            dfs(nextNode,count+1)
            visited[nextNode]=False


n,m=map(int,input().split())
graph=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)

for i in range(n):
    visited=[False for i in range(n)]
    visited[i]=True
    dfs(i,1)
print(0)

'''
백트래킹을 써야 하는 문제면 백트래킹을 쓰자

백트래킹 vs bfs
후자는 시작점에서 a점에 갈 수 있는 "최소비용" 구하기. 네트워크처럼 한 줄은 아님
⭐️전자는 "하나의 이어지는 줄" 구하기⭐️

'''