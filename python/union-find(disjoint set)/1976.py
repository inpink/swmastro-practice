import sys
input=sys.stdin.readline


def find(x):
    if vRoot[x] != x:
        vRoot[x] = find(vRoot[x])
    return vRoot[x]


n=int(input())
m=int(input())

vRoot = [ i for i in range(n)]

for i in range(n):
    connect=list(map(int,input().split()))

    for j in range(n):
        if connect[j]==1:
            # union-find로 연결 (i와 j는 연결돼있다)
            iParent=find(i)
            jParent=find(j)

            if iParent!=jParent:
                vRoot[jParent] = iParent
    #print(vRoot)


plans=list(map(int,input().split()))

answer=[]
for city in plans:
    cityParent=find(city-1)
    answer.append(cityParent)

#print(answer)

if (len(set(answer))==1):
    output="YES"
else:
    output="NO"

print(output)

