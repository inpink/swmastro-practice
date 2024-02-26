import sys
input=sys.stdin.readline

from collections import deque

n=int(input())
q=deque()
for i in range(n):
    order=list(map(int,input().split()))
    #print(order)


    if order[0]==1:
        q.appendleft(order[1])
    elif order[0]==2:
        q.append(order[1])
    elif order[0]==3:
        if len(q)!=0:
            print(q.popleft())
        else:
            print(-1)
    elif order[0]==4:
        if len(q)!=0:
            print(q.pop())
        else:
            print(-1)
    elif order[0]==5:
        print(len(q))
    elif order[0]==6:
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif order[0]==7:
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif order[0]==8:
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])

    #print(q)