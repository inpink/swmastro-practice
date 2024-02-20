'''
1261이랑 동일한 문제
'''
import sys
input = sys.stdin.readline
from collections import deque

n=int(input())

graph=[]
for i in range(n):
    row=list(map(int,input().rstrip()))
    graph.append(row)

#for i in graph:
    #print(i)

# 0-1 bfs
q=deque()
visited=[[False for i in range(n)] for i in range(n)]
count=0
direction=[(-1,0),(1,0),(0,-1),(0,1)] #상 하 좌 우

q.append((0,0,0)) #count, start x,y
visited[0][0]=True

while True:
    if len(q)==0:
        break

    curCount,curX,curY=q.popleft()

    if curX==n-1 and curY==n-1:
        count=curCount
        break

    for moveX,moveY in direction:
        nextX=curX+moveX
        nextY=curY+moveY

        if nextX<0 or nextX>=n or nextY<0 or nextY>=n:
            continue
        if visited[nextX][nextY]:
            continue

        if graph[nextX][nextY]==1:
            q.appendleft((curCount,nextX,nextY))
            visited[nextX][nextY]=True
        elif graph[nextX][nextY]==0:
            q.append((curCount+1,nextX,nextY))
            visited[nextX][nextY]=True
    #print(q)
print(curCount)
