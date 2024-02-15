'''
BOJ G5 stack 문제 2 try

이 문제의 핵심
1) 코드가 좀 지저분해지더라도 확실하게 풀리도록 하자
=> 논리의 오류가 없게 (중복되는 코드 분명히 나중에 본다면 줄일 수 있지만 이는 리팩터링할 시간이 있을 때 하는 것.
이번 문제에서는 쭉 나열하더라도 각 경우를 쉽게 파악할 수 있다는 장점도 가짐)
=> ⭐️ 중간에 break가 되는 경우, 따로 bool형 변수를 둬서 False인 경우 무조건 ans을 0으로 주는 코드를 추가하자.
    (이번 문제 이거 때문에 틀림)

'''
import sys
from collections import deque
input = sys.stdin.readline

def plusNumber(stack):
    # 숫자 만들어졌을 때 앞이 숫자면 합치기
    if (len(stack)==1):
        return
    elif (str(stack[-2]).isdigit()):
        num1=stack[-2]
        num2=stack[-1]
        stack.pop()
        stack.pop()
        stack.append(num1+num2)

s=input().rstrip()
splited=deque([char for char in s])
size=len(s)
stack=[]
ans=0
match=True

for i in range(size):
    new=splited.popleft()
    #print(new)
    if (len(stack)==0):
        if (new==']' or new==')'):
            ans=0
            match=False
            break
        else:
            stack.append(new)
    else:
        top=stack[-1]
        if (new==')'):
            if (top=='('):
                stack.pop()
                stack.append(2)
                # 숫자 만들어졌을 때 앞이 숫자면 합치기
                plusNumber(stack)

            elif (top=='['):
                ans=0
                match=False
                break
            elif (str(top).isdigit()):
                # 괄호 판단해서 곱셈 연산 해야함
                if (len(stack)==1): # 3 )
                    ans=0
                    match=False
                    break
                elif (stack[-2]=='('):
                    stack.pop()
                    stack.pop()
                    stack.append(top*2)
                    # 숫자 만들어졌을 때 앞이 숫자면 합치기
                    plusNumber(stack)

                elif (stack[-2]=='['):
                    ans=0
                    match=False
                    break
        elif (new==']'):
            if (top=='['):
                stack.pop()
                stack.append(3)
                # 숫자 만들어졌을 때 앞이 숫자면 합치기
                plusNumber(stack)

            elif (top=='('):
                ans=0
                match=False
                break
            elif (str(top).isdigit()):
                # 괄호 판단해서 곱셈 연산 해야함
                if (len(stack)==1): # 3 ]
                    ans=0
                    match=False
                    break
                elif (stack[-2]=='['):
                    stack.pop()
                    stack.pop()
                    stack.append(top*3)
                    # 숫자 만들어졌을 때 앞이 숫자면 합치기
                    plusNumber(stack)

                elif (stack[-2]=='('):
                    ans=0
                    match=False
                    break

        elif (new=='(' or new=='['):
            stack.append(new)

    #print(stack)
    #print()

if match==True: # 끝까지 모든 경우를 검사함
    if (len(stack)==1 and str(stack[0]).isdigit()):
        ans=stack[0]
    else:
        ans=0
else:
    ans=0

print(ans)
'''
s : 길이는 1 이상, 30 이하
입력이 올바르지 못한 괄호열이면 반드시 0을 출력

(()[[]])([])
(2[3]
(2 9
(11)
'''