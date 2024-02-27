import sys
input=sys.stdin.readline

import heapq
n=int(input())
nums=[]
for i in range(n):
    num=int(input())
    heapq.heappush(nums,num)

if len(nums)==1:
    print(0)
else:
    ans=0
    while True:
        if len(nums)==1:
            break
        #print(nums)
        num1=heapq.heappop(nums)
        num2=heapq.heappop(nums)
        ans+=(num1+num2)
        #print(ans,num1,num2)
        heapq.heappush(nums,num1+num2)
    print(ans)

'''
정렬된 두 묶음의 숫자 카드
각 묶음의 카드의 수 A,B
두 묶음을 합쳐서 하나로 만드려면 A+B번의 비교를 해야한다?

매우 많은 숫자 묶음들
두 묶음씩 골라 서로 합쳐나간다 => 이때 고르는 순서에 따라 비교횟수 매우 달라짐
예를들어 10,20,40 => 10+20  30+40 =100  / 10+40 50+20=120

최소횟수를 구할것
N은 1~10만 
각 크기는 1~1000 


반례)
4
1
1
1
1
=> 1+1+2+1+3+1로 9이 아닌, 1+1+1+1+2+2로 8
'''