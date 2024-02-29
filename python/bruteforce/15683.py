import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
oneCCTV=[]
twoCCTV=[]
threeCCTV=[]
fourCCTV=[]
fiveCCTV=[]
total=[]
squareArea=0
for i in range(n):
    row=list(map(int,input().split()))
    graph.append(row)
    for j in range(m):
        num=row[j]
        if num==0:
            squareArea+=1
        if num==1:
            oneCCTV.append((i,j))
            total.append((1,i,j))
        elif num==2:
            total.append((2,i,j))
            twoCCTV.append((i,j))
        elif num==3:
            total.append((3,i,j))
            threeCCTV.append((i,j))
        elif num==4:
            total.append((4,i,j))
            fourCCTV.append((i,j))
        elif num==5:
            total.append((5,i,j))
            fiveCCTV.append((i,j))

#for i in graph:
    #print(i)

one=["u","d","l","r"] #상,하,좌,우
two=["ud","lr","ud","lr"] #상하, 좌우 (편의상 4개로 맞춰줌)
three=["ur","rd","dl","lu"]
four=["lur","urd","ldr","dlu"]
five=["udlr","udlr","udlr","udlr"]
direction={"u":(-1,0),"d":(1,0),"l":(0,-1),"r":(0,1)}
totalDirection={1:one,2:two,3:three,4:four,5:five}

totalSize=len(total)

from itertools import product

products=list(product(range(4),repeat=totalSize))
#print("products:",products)
'''
print(oneCCTV)
print(twoCCTV)
print(threeCCTV)
print(fourCCTV)
print(total)
'''
minV=65
for pro in products: #0 0 0 0
    #deepcopy
    newGraph=[[]for i in range(n)]
    for i in range(n):
        for j in range(m):
            newGraph[i].append(graph[i][j])
    count=0
    for i in range(totalSize): #
        cctvNum,cctvX,cctvY=total[i] # 1 0 1

        #print(total[i],totalDirection[cctvNum][pro[i]])
        for order in totalDirection[cctvNum][pro[i]]: #udlr
            moveX,moveY=direction[order]
            nextX=cctvX
            nextY=cctvY

            while True:
                nextX=nextX+moveX
                nextY=nextY+moveY

                if nextX==cctvX and nextY==cctvY:
                    continue
                if nextX<0 or nextX>=n or nextY<0 or nextY>=m:
                    break
                if newGraph[nextX][nextY]==6:
                    break
                if newGraph[nextX][nextY]==0:
                    newGraph[nextX][nextY]='#'
                    count+=1
    #for aaa in newGraph:
        #print(aaa)

    minV=min(minV,squareArea-count)
    #print(count,squareArea-count)
print(minV)
'''
0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호

CCTV의 방향을 적절히 정해서
사각 지대의 최소 크기를 구하는 프로그램을 작성
'''