import sys
input=sys.stdin.readline
import math

n,m=map(int,input().split())
booksInput=list(map(int,input().split()))
booksInput.sort()
minusBooks=[]
plusBooks=[]
for i in range(n):
    book=booksInput[i]
    if book<0:
        minusBooks.append(book)
    else:
        plusBooks.append(book)
#print(minusBooks,plusBooks)

if len(minusBooks)==0:
    minusBooks=[0]
if len(plusBooks)==0:
    plusBooks=[0]
maxAbs=max(abs(min(minusBooks)),max(plusBooks))
#print(maxAbs)
maxCount=1

minusBundleCount=math.ceil(len(minusBooks)/m)
plusBundleCount=math.ceil(len(plusBooks)/m)
#print(minusBundleCount,plusBundleCount)

ans=0
# minus 계산
for i in range(minusBundleCount):
    start=i*m
    if maxCount==1 and abs(minusBooks[start])==maxAbs:
        maxCount=0
        ans+=abs(minusBooks[start])
    else:
        ans+=abs(minusBooks[start])*2
    #print(ans)

# plus 계산
plusBooks.sort(reverse=True)
for i in range(plusBundleCount):
    start=i*m
    if maxCount==1 and abs(plusBooks[start])==maxAbs:
        maxCount=0
        ans+=abs(plusBooks[start])
    else:
        ans+=abs(plusBooks[start])*2
print(ans)
'''
그리디

음수와 양수는 함께 들고가는걸 계산할 필요가 없다 
어차피 2a+2b니까 따로보기


음수+양수 절대값이 가장 큰 숫자가 돌아오지 않고 끝나는 지점이 됨
2a 2b에서 a>b면 a+2b가 항상 2a+b보다 작으니까

음수/양수 나눠서 절대값 큰수대로 m개만큼 묶음
전체에서 가장 큰 수 제외하고 묶음의 절대값 가장 큰 수 *2 
 

'''
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