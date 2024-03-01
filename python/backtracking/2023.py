import sys
input=sys.stdin.readline

#print(3*5**7)

decimalSet=set()

def isDecimal(x):
    if x==1:
        return False
    if x==2:
        return True

    if x in decimalSet:
        return True

    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False

    decimalSet.add(x)
    return True

def dfs(numStr):
    #print(numStr)
    if len(numStr)==n:
        if isDecimal(int(numStr)):
            ansList.append(int(numStr))
        return

    for i in "123579":
        nextNumStr=numStr+i
        if isDecimal(int(nextNumStr)):
            dfs(nextNumStr)

ansList=[]
n=int(input())
#visited=[False for i in range()]
dfs("")
ansList.sort()
for i in ansList:
    print(i)
'''
N자리 신기한 소수를 모두 찾아보자. N(1 ≤ N ≤ 8)

이 문제 역시 ⭐️앞쪽에서 겹치는 요소들⭐️ 덕분에 백트래킹이 훨씬 효율적임
'''