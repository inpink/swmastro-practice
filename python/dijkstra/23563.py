import sys
input=sys.stdin.readline
import heapq

def isFree(x,y,h,w):
    isPossible=False
    for moveX,moveY in direction:
        closeX=x+moveX
        closeY=y+moveY

        if closeX<0 or closeX>=h or closeY<0 or closeY>=w:
            continue

        if graph[closeX][closeY]=='#':
            isPossible=True
            break

    return isPossible

maxValue= sys.maxsize
h,w=map(int,input().split())

graph=[]
for i in range(h):
    row=list(map(str,input().rstrip()))
    graph.append(row)

    for j in range(w):
        if graph[i][j]=='S':
            start=(i,j)
        elif graph[i][j]=='E':
            end=(i,j)

#for i in graph:
    #print(i)

dp=[[maxValue for i in range(w)] for i in range(h)]
direction = [(-1,0),(1,0),(0,-1),(0,1)] #상 하 좌 우
heap=[]
heapq.heappush(heap,[0,start[0],start[1]]) #cost, startX, Y
#print(start,end,heap)

while True:
    if len(heap)==0:
        break

    curCost, curX, curY=heapq.heappop(heap)

    if curX==end[0] and curY==end[1]:
        break

    for moveX,moveY in direction:
        nextX=curX+moveX
        nextY=curY+moveY

        if nextX<0 or nextX>=h or nextY<0 or nextY>=w:
            continue
        if graph[nextX][nextY]=='#':
            continue

        if isFree(curX,curY,h,w) and isFree(nextX,nextY,h,w):
            if dp[nextX][nextY]>curCost:
                dp[nextX][nextY]=curCost
                heapq.heappush(heap,[curCost,nextX,nextY])
        else:
            if dp[nextX][nextY]>curCost+1:
                dp[nextX][nextY]=curCost+1
                heapq.heappush(heap,[curCost+1,nextX,nextY])

#for i in dp:
    #print(i)
print(dp[end[0]][end[1]])


'''
 $H$개의 행과 $W$개의 열 (1~500)
  상, 하, 좌, 우 방향 인접한 칸으로 한 칸씩 이동할 수 있다. 벽으로는 이동할 수 없다.
  한 칸을 이동하는 데에는 1초가 걸린다.
  벽을 타고 이동하면 순식간에 (0초의 시간에) 상, 하, 좌, 우 방향 인접한 칸으로 이동할 수 있다.
  어떤 빈칸의 상하좌우 중 하나가 벽이면 이 칸은 벽에 인접한 칸
  벽에 인접한 칸에서 벽에 인접한 칸으로 이동하면 벽을 타고 이동한다
  
  루시우가 맵의 시작점에서 끝점까지 이동하는 데 걸리는 최소 시간을 구하여라.
  #는 벽을 뜻한다.
  .는 빈칸을 뜻한다.
  S는 맵의 시작점을 뜻한다. 시작점은 빈칸이다.
E는 맵의 끝점을 뜻한다. 끝점은 빈칸이다.

시작점 S와 끝점 E는 각각 하나씩만 주어진다.
맵의 가장 바깥 (1번째 열, $W$번째 열, 1번째 행, $H$번째 행) 칸들은 모두 벽이다.
시작점에서 끝점까지 이동할 수 없는 경우는 주어지지 않는다.


4 3
###
#S#
#E#
### 

0

----

6 5
#####
#...#
#.S.#
##..# 
#E..#
#####

1


----

6 5
#####
#S..#
#..##
##..# 
#E..#
#####

0
'''