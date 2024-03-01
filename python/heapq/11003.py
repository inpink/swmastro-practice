import sys
input=sys.stdin.readline

n,l=map(int,input().split())
nums=list(map(int,input().split()))
ansList=[]
import heapq

heap=[]
for i in range(n):
    num=nums[i]
    heapq.heappush(heap,(num,i))
    while True:
        topNum,topI=heap[0]
        if i-topI>=l:
            heapq.heappop(heap)
        else:
            ansList.append(topNum)
            break

print(*ansList)