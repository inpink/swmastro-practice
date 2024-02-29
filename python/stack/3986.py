import sys
input=sys.stdin.readline

n=int(input())
count=0
for i in range(n):
    s=input().rstrip()

    stack=[]
    for al in s:
        if len(stack)==0:
            stack.append(al)
        else:
            if stack[-1]==al:
                stack.pop()
            else:
                stack.append(al)
    if len(stack)==0:
        count+=1
        #print("dd")
print(count)

'''
모든 글자가 A,B로 바뀜
"좋은 글자"를 세어보기로 함

1) A__A_AA를 묶을 때, A끼리는 어떻게 묶든 교차되지 않게 구현 가능
즉, 같은 문자끼리는 선 교차의 문제가 안됨
2) 다른 문자끼리의 선 교차가 문제임
그렇다면 같은 문자를 최대한 크게 묶거나 최대한 작게묶는것이 좋을까?
작게 묶어도 된다. ABA... ABBA... 에서 A를 최대한 가까운 A에 묶든 멀리있는걸 묶든
A가 다른 A를 만나기 전에 B가 있는데 그 B가 다른 A를 만나기 전에 매칭이 안된다면
어차피 선분 교차하기 때문임
==> ⭐️ 스택 문제 잘 기억해두기
'''