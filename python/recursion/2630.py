import sys
input=sys.stdin.readline

colors=[0,0] #white,blue
def solution():
    n=int(input())
    graph=[]
    for i in range(n):
        row=list(map(int,input().split()))
        graph.append(row)
    #print(graph)

    rec(graph,0,0,n,n)
    print(colors[0])
    print(colors[1])

def isFull(graph,startX,startY,endX,endY): #0,0,2,2  4,4,6,6
    before=graph[startX][startY]
    for i in range(startX,endX):
        for j in range(startY,endY):
            if graph[i][j]!=before:
                return False
    return True

def rec(graph,startX,startY,endX,endY):
    #print(startX,startY,endX,endY)
    if isFull(graph,startX,startY,endX,endY)==True:
        colors[graph[startX][startY]]+=1
        return

    line=endX-startX
    half=line//2
    rec(graph,startX,startY,startX+half,startY+half) #왼위
    rec(graph,startX+half,startY,endX,startY+half) #오른위
    rec(graph,startX,startY+half,startX+half,endY) #왼아래
    rec(graph,startX+half,startY+half,endX,endY) #오른아래



solution()

'''
파란색 1
하얀색 0

다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다.

전체 종이의 크기가 N×N(N=2k, k는 1 이상 7 이하의 자연수)  (N은 2, 4, 8, 16, 32, 64, 128 중 하나
전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 <그림 2>의 I, II, III, IV와 같이 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다.
이와 같은 과정을 1)잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 
2)하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.

잘라진 하얀색 색종이와 파란색 색종이의 개수 각각 구하기

매번 모든 판을 검사해도 2**7*7번이라 괜찮
2**?=n이면 ?번만큼 최대 자를 수 있음
자를 때마다 재귀 가지가 4개씩 생기므로
깊이가 ?일 때 1+4+16+64... +4**(?-1) = 4**? 정도의 재귀 호출
4**7=16000정도로 OK 
'''