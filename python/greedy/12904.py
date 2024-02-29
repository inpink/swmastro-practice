import sys
input=sys.stdin.readline

import heapq
from collections import deque

s=deque(list(map(str,input().rstrip())))
t=deque(list(map(str,input().rstrip())))
#print(s,t)
heap=[(-len(t),t)]

sSize=len(s)
ans=0
while True: #최대 1000번
    #print(heap[0])
    if len(heap)==0:
        break
    if -heap[0][0]<sSize:
        break
    topLen,topDeq=heapq.heappop(heap)

    if -topLen==sSize and s==topDeq:
        ans=1
        break

    #문자열의 맨 뒤에 A를 뺀다
    if topDeq[-1]=='A':
        forA=deque(topDeq)
        forA.pop()
        heapq.heappush(heap,(topLen+1,forA))

    #문자의 맨 뒤에 B를 빼고 뒤집는다
    if topDeq[-1]=='B':
        forB=deque(topDeq)
        forB.pop()
        forB.reverse()
        heapq.heappush(heap,(topLen+1,forB))


print(ans)