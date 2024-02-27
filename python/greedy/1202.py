import sys
input=sys.stdin.readline

n,k=map(int,input().split())
gems=[]
for i in range(n):
    m,v=map(int,input().split())
    gems.append([m,v])

bags=[]
for i in range(k):
    c=int(input())
    bags.append(c)

#작은 가방을 먼저 채워야 한다
#각 가방마다, 선택 가능한 gems들 중 가장 price가 높은 값을 뽑자
import heapq
bags.sort()
heapq.heapify(gems)

ans=0
candis=[]
for bag in bags:
    while True:
        if len(gems)==0:
            break
        if gems[0][0]>bag:
            break

        gemW,gemP=heapq.heappop(gems)
        heapq.heappush(candis,[-gemP,gemW])
    if len(candis)>0:
        ans+=(-heapq.heappop(candis)[0])
print(ans)

'''
보석은 총 N개
각 보석은 무게 M, 가격 V

가방 K개
각 가방에는 보석 1개만
각 가방에는 무게C까지만 담을 수 있음

훔칠 수있는 보석의 최대 "가격"


비싼걸 담아야 하는데 => 무게a와 딱 맞는 가방이 있으면 고민없이 선택하면 되지만
무게a보다 큰 가방만 있을땐 얘때문에 다른 가방이 비어버리면 오히려 손해일수도있고 손해아닐수도있고
(=가방이 비어있을수도 있다)
아닌거같은데?

작은 무게 가방부터 봐서
여기에 들어갈수있는 애들 중 가장 비싼

일단 비싼놈을 먼저 포커스해보자 
O(N+K)정도로 끝내야하는데
대체 한번 순회해서 어떻게 구하지 
'''