import sys
from collections import deque
input = sys.stdin.readline

s=input().rstrip()
bomb = input().rstrip()

splited= deque([char for char in s])

s_size=len(s)
bomb_size=len(bomb)

stack=[]

for i in range(s_size):
    stack.append(splited.popleft())

    if (len(stack)<bomb_size):
        continue

    possible=True
    for j in range(bomb_size):
        if stack[len(stack)-bomb_size+j]!=bomb[j]:
            possible=False
            break

    if possible:
        for k in range(bomb_size):
            stack.pop()

if (len(stack)==0):
    ans="FRULA"
else:
    #ans=reduce(lambda x,y:x+y,stack) #시간초과
    ans="".join(stack)


print(ans)
'''
모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해
남아있는 문자가 없는 경우 "FRULA"를 출력
폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.

s 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.
bomb  길이는 1보다 크거나 같고, 36보다 작거나 같다.

s 하나 넣을 때마다 bomb 모든문자 한번씩 검사해도
36회x100만회라 3600만회밖에 안됨

두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만

⭐️ 스택 문제!! 
앞에서 하나하나 쌓아가니까!


mirkovC4nizCC44
mirko
'''