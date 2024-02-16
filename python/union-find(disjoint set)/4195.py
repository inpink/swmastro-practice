import sys
input = sys.stdin.readline

def indexing(name,names):
    if name not in names:
        names[name]=len(names)
    return names[name]

def find(x):
    if vRoot[x]!=x:
        vRoot[x]=find(vRoot[x])
    return vRoot[x]

t=int(input())

for i in range(t):
    f=int(input())

    vRoot=[i for i in range(f*2)]
    groupCounts=[1 for i in range(f*2)]
    names=dict()
    for j in range(f):
        a,b=map(str,input().split())

        indexedA,indexedB=indexing(a,names), indexing(b,names)

        #print(names)
        #print(indexedA,indexedB)

        #if vRoot[indexedA]!=vRoot[indexedB]: #⭐️
        aParent=find(indexedA)
        bParent=find(indexedB)

        vRoot[bParent]=aParent

        if aParent!=bParent:
            groupCounts[aParent]+=groupCounts[bParent]
            groupCounts[bParent]=0 # aParent==bParent일 경우 문제가 될 수 있음

        print(vRoot)
        print(groupCounts)
        print()

        #친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는
        # union-find 모두 업데이트
        # ⭐️ 이것도 시간초과
        #for p in range(len(names)):
            #vRoot[p]=find(p)
        #print(vRoot)

        # ⭐️ 여기서 하나하나 세주면 10만x10만=100억으로 시간초과
        '''count=0
        for k in range(len(names)):
            if vRoot[k]==vRoot[indexedA]:
                count+=1
        print(count)'''

        print(groupCounts[aParent])
    #print("#")