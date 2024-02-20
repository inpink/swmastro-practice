'''
0으로는 비용 0으로 이동할 수 있고
벽이 있으면 비용 1으로 이동할 수 있다
=> 0-1 bfs로, 비용 0인 경우를 우선 탐색해야 함
'''

import sys
input = sys.stdin.readline
from collections import deque

m,n=map(int,input().split())

graph=[]
for i in range(n):
    row=list(map(int,input().rstrip()))
    graph.append(row)

#for i in graph:
    #print(i)

# 0-1 bfs
q=deque()
visited=[[False for i in range(m)] for i in range(n)]
count=0
direction=[(-1,0),(1,0),(0,-1),(0,1)] #상 하 좌 우

q.append((0,0,0)) #count, start x,y
visited[0][0]=True

while True:
    if len(q)==0:
        break

    curCount,curX,curY=q.popleft()

    if curX==n-1 and curY==m-1:
        count=curCount
        break

    for moveX,moveY in direction:
        nextX=curX+moveX
        nextY=curY+moveY

        if nextX<0 or nextX>=n or nextY<0 or nextY>=m:
            continue
        if visited[nextX][nextY]:
            continue

        if graph[nextX][nextY]==0:
            q.appendleft((curCount,nextX,nextY))
            visited[nextX][nextY]=True
        elif graph[nextX][nextY]==1:
            q.append((curCount+1,nextX,nextY))
            visited[nextX][nextY]=True
    #print(q)
print(curCount)
'''
0은 빈 방을 의미하고, 1은 벽을 의미한다.
가로 크기 M, 세로 크기 N
'''