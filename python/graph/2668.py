import sys
input=sys.stdin.readline

def dfs(root,start,count):
    #print(root,start,count)
    if visited[root] and start==root:
        #print("찾음")
        return (True,count)
    next=graph[start]
    if visited[next]==True:
        return (False,-1)

    visited[next]=True
    possible,ans=dfs(root,next,count+1)

    return (possible,ans)

graph=dict()
n=int(input())
sames=[]
for i in range(1,n+1):
    graph[i]=int(input())
    if i==graph[i]:
        sames.append(i)
#print(graph)

maxValue=-1
maxSet=set()
for i in range(1,n+1):
    visited=[False for i in range(n+1)]
    for same in sames:
        visited[same]=True
    possible,ans=dfs(i,i,0)
    if possible:
        #print("업데이트")
        for j in range(1,n+1):
            if visited[j]:
                maxSet.add(j)
        maxValue=ans
print(len(maxSet))
maxList=list(maxSet)
maxList.sort()
for i in maxList:
    print(i)
'''
start->a->b->start
로 돌아와야함

start->a->b->a같은경우 정답이 나오지 않는 사이클발생으로 X

=> dfs
시간복잡도 100*100 매우짧음
'''