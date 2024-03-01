import sys
input=sys.stdin.readline

n=int(input())

graph=[]
for i in range(n):
    row=list(map(int,input().split()))
    graph.append(row)

from itertools import permutations

perms=list(permutations(range(0,n),n))
print(perms)
minV=10**10
for perm in perms:
    start=perm[0]
    possible=True
    sumCost=0
    for i in range(n):
        start=perm[i%n]
        next=perm[(i+1)%n]
        if graph[start][next]==0:
            possible=False
            break
        sumCost+=graph[start][next]
        if sumCost>=minV:
            possible=False
            break
    if possible:
        minV=min(minV,sumCost)
    #print(perm,sumCost,minV)
print(minV)

