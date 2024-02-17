import sys
input=sys.stdin.readline

def find(x):
    if vRoot[x]!=x:
        vRoot[x]= find(vRoot[x])
    return vRoot[x]

n,m,k=map(int,input().split())

fee = [0]+list(map(int,input().split()))
#print(fee)

vRoot=[i for i in range(n+1)]

for i in range(m):
    v,m=map(int,input().split())

    vParent=find(v)
    mParent=find(m)

    if vParent!=mParent:
        vRoot[mParent]=vParent

#print(vRoot)

group=[[] for i in range(n+1)]
for i in range(1,n+1):
    iParent=find(i)

    group[iParent].append((fee[i],i))

#print(group)

need=0
for groupSet in group:
    if len(groupSet)!=0:
        minFee,minIndex = min(groupSet, key=lambda x:x[0] )
        #print(minFee)
        need+=minFee

if need<=k:
    ans=need
else:
    ans="Oh no"

print(ans)
'''
 학생이 N명인 학교  N (1 ≤ N ≤ 10,000)
 학생 i에게 Ai만큼의 돈을 주면 그 학생은 1달간 친구가 되어준다
 준석이에게는 총 k원의 돈이 있고 k (1 ≤ k ≤ 10,000,000)
 “친구의 친구는 친구다”
 가장 적은 비용으로 모든 사람과 친구가 되는 방법구하라.

친구관계 수 M (0 ≤ M ≤ 10,000)

N개의 각각의 학생이 원하는 친구비 Ai (1 ≤ Ai ≤ 10,000, 1 ≤ i ≤ N)

v와 학생 w가 서로 친구라는 뜻이다.
자기 자신과 친구일 수도 있고
같은 친구 관계가 여러 번 주어질 수도 있다.


준석이가 모든 학생을 친구로 만들 수 있다면, 친구로 만드는데 드는 최소비용을 출력한다
만약 친구를 다 사귈 수 없다면, “Oh no”(따옴표 제거)를 출력한다.


'''