import sys
input=sys.stdin.readline
from collections import deque

t=int(input())

for i in range(t):
    l=input().rstrip()
    size=len(l)
    splited=deque([char for char in l])
    left=[]
    right=[]

    for j in range(size):
        word=splited.popleft()

        if word=='<':
            if len(left)!=0:
                right.append(left.pop())
        elif word=='>':
            if len(right)!=0:
                left.append(right.pop())
        elif word.isalpha() or word.isdigit():
            left.append(word)
        elif word=='-':
            if len(left)!=0:
                left.pop()

    #print(left,right)
    # left right 합쳐서 정답 구하기
    ans= "".join(left) + "".join(right[::-1])

    print(ans)



'''
키로거는 사용자가 키보드를 누른 명령을 모두 기록한다.
 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표
비밀번호의 길이는 항상 0보다 크다.

지울 때, 만약 커서의 위치가 줄의 마지막이 아니라면, 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.
<- 이게 뭔소리?

ABCD<-- 
정답 A,D
'''