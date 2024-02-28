import sys
input=sys.stdin.readline

def rec(standard,startX,startY,count,c,r):
    #print(standard,startX,startY,count)
    if not (startX<=c and startY<=r and startX+standard>c and startY+standard>r):
        return

    if startX==c and startY==r:
        print(count)
        exit(0)


    rec(standard//2,startX,startY,count+standard*standard//4*0,c,r) #왼위
    rec(standard//2,startX,startY+standard//2,count+standard*standard//4*2,c,r)  #오른위
    rec(standard//2,startX+standard//2,startY,count+standard*standard//4*1,c,r) #왼아래
    rec(standard//2,startX+standard//2,startY+standard//2,count+standard*standard//4*3,c,r)

n,r,c=map(int,input().split())

rec(2**n,0,0,n*n//4*0,c,r)
