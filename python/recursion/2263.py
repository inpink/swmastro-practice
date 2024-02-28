import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def rec(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return

    root=postOrders[postEnd]
    print(root,end=' ')

    leftCount=map[root]-inStart
    rightCount=inEnd-map[root]

    rec(inStart, inStart + leftCount - 1, postStart, postStart + leftCount - 1)
    rec(inEnd-rightCount+1,inEnd,postEnd-rightCount,postEnd-1)

n=int(input())
inOrders=list(map(int,input().split()))
postOrders=list(map(int,input().split()))

map=['' for i in range(n+1)]
for i in range(n):
    map[inOrders[i]]=i
rec(0,n-1,0,n-1)