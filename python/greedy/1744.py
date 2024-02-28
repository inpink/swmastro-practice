import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
posiNums=[]
negaNums=[]
ones=[]
zeros=[]
allNums=[]
for i in range(n):
    num=int(input())
    allNums.append(num)
    if num>1:
        posiNums.append(num)
    elif num==1:
        ones.append(num)
    elif num==0:
        zeros.append(num)
    else:
        negaNums.append(num)
posiNums.sort(reverse=True)
negaNums.sort()
posiNums=deque(posiNums)
negaNums=deque(negaNums)
#print(posiNums)
#print(negaNums)

if n==1:
    print(allNums[0])
    exit(0)

ans=0

#2 이상 양수 처리
posiCount=len(posiNums)//2
for i in range(posiCount):
    ans+=(posiNums.popleft()*posiNums.popleft())

if len(posiNums)>0:
    ans+=posiNums.popleft()


#1 처리
ans+=(sum(ones))

# 음수 처리
negaCount=len(negaNums)
for i in range(negaCount//2):
    ans+=(negaNums.popleft()*negaNums.popleft())


# 음수와 0 처리
zeroCount=len(zeros)
negaCount=len(negaNums)
for i in range(min(zeroCount,negaCount)):
    negaNums.popleft()

ans+=(sum(negaNums))
print(ans)

'''
0이 있으면 가장 큰 음수랑 곱하기
0이 있는데 음수가 없으면 냅두기
음수는 양수와 곱하면 무조건 손해 0없으면 건들지말기
음수끼리 곱하면 더 큰수가 될 수 있음

이제 양수만 정하면 됨
a,b,c인데 a<b<c이면 무조건 b*c를 곱하는게 낫다 (수식 증명 가능) 아 그리디는 찍는게 아니라 증명하는거구나

1은 누구랑도 곱하면 무조건 손해임


'''