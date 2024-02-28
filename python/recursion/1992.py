import sys
input=sys.stdin.readline

def isFull(standard,startX,startY):
    before=map[startY][startX]
    for i in range(startX,startX+standard):
        for j in range(startY,startY+standard):
            if map[j][i]!=before:
                return False
    return True

def rec(standard,startX,startY):
    if isFull(standard,startX,startY):
        print(map[startY][startX],end='')
        return

    print("(",end='')
    rec(standard//2,startX,startY) #좌상
    rec(standard//2,startX+standard//2,startY) #우상
    rec(standard//2,startX,startY+standard//2) #좌하
    rec(standard//2,startX+standard//2,startY+standard//2)#우하
    print(")",end='')

n=int(input())
map=[]
for i in range(n):
    row=input().rstrip()

    map.append([row[i] for i in range(n)])
print(map)
rec(n,0,0)