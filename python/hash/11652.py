'''
숫자 카드 N장  N (1 ≤ N ≤ 100,000)
적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같은 정수
가장 많이 가지고 있는 정수를 구하는 프로그램
만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력
'''

import sys
input = sys.stdin.readline

n=int(input())
dic=dict()
for i in range(n):
    num=int(input())

    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1

#print(dic)
print(max(dic,key=lambda x:(dic[x],-x)))