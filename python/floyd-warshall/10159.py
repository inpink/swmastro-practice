import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

maxValue=10**8
graph=[[maxValue for i in range(n+1)]for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split()) #a<-b  더큰숫자에게 속함
    graph[a][b]=1 #a가 b를 이긴다

for k in range(1,n+1):
    for i in range(1,n+1):
        if graph[i][k]==maxValue:
            continue
        for j in range(1,n+1):
            if graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j]=graph[i][k]+graph[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]!=maxValue:
            graph[j][i]=-graph[i][j]

for i in range(1,n+1):
    graph[i][i]=0
#print()
#for i in graph:
#    print(i)

for i in range(1,n+1):
    count=0
    for j in range(1,n+1):
        if graph[i][j]==maxValue:
            count+=1
    print(count)