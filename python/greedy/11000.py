import sys
input=sys.stdin.readline

'''
⭐️ 풀이 생각하기 어려웠던 문제
heap에는 사용중인 class를 담는다, heap은 **끝나는 시간이 빠른 순서대로** 정렬한다
times는 **시작하는 시간이 빠른 순서대로** 정렬한다
=> 끝나는 시간, 시작하는 시간 2개가 맞닿는 걸 최대한 많이 해주기 위함!!
times에서 순서대로 하나하나 꺼낸 모든 class는 heap에 들어간다.
하지만, 만약 heap[0]인 ***가장 먼저 끝나는 class***의 끝나는 시간< 새로 넣을 현재로서 가장 빨리 시작하는 class 시작시간
이라면 강의실 개수가 늘어날 필요가 없으므로, 이 강의실을 heap에서 빼고 새로운 강의를 heap에 넣어준다.
마지막으로 heap 길이를 출력하면 사용된 최소의 강의실 개수가 나온다

- 20만, 30만같은 숫자가 나오면 트리구조 생각하기. nlog2n일 가능성 높음. 
  - for문 내부에 heappush나 heappop쓰거나
  - for문 내부에 2배씩 줄어드는 while문 쓰거나
'''
n=int(input())
times=[]
for i in range(n):
    s,t=map(int,input().split())
    times.append([s,t])
times.sort()
#print(times)

import heapq
heap=[]
heapq.heappush(heap,[times[0][1],times[0][0]])
for i in range(1,n):
    thisClassStart,thisClassEnd=times[i]
    if heap[0][0]<=thisClassStart:
        heapq.heappop(heap)
    heapq.heappush(heap,[thisClassEnd,thisClassStart])
    #print(heap)
print(len(heap))