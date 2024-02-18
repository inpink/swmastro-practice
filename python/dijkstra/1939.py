import sys
import heapq
input = sys.stdin.readline

n,m=map(int,input().split())
maxValue=sys.maxsize
#print(min)

# ⭐ n이 1만이라, 1만x1만=1억 개만큼 미리 만들어두면 메모리 초과!!!!
# 10만개의 간선을 넣어주는게 메모리적으로 더 효율적!
graph=[[] for i in range(n+1)]


for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

#for i in graph:
    #print(i)

start,end=map(int,input().split())

# 다익스트라
heap=[]
dp=[0 for i in range(n+1)]
heapq.heappush(heap, (-maxValue,start))
#print(dp)
while True:
    if len(heap)==0:
        break

    cost, node = heapq.heappop(heap)

    if node==end: # 큰 것부터 뽑고, 각 연산에서 min값을 구하므로 먼저 도착했을 때가 항상 최댓값
        break

    for arriveNode, arriveCost in graph[node]:
        nextCost =-min(arriveCost,-cost)
        if dp[arriveNode]>nextCost:
            dp[arriveNode]=nextCost
            heapq.heappush(heap,(nextCost,arriveNode))
    #print("dp:",dp, heap)

print(-dp[end])
'''
문제를 제대로 읽자!!!! 경로들의 cost 합이 아니라, 
여러 경로를 거친다면 경로들 중 최솟값이다.


N(2 ≤ N ≤ 10,000)개의 섬
몇 개의 섬 사이에는 다리 M(1 ≤ M ≤ 100,000)가 설치되어 있어서 차들이 다닐 수 있다.
 각각의 다리마다 중량제한
 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램


서로 같은 두 섬 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향
 마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다.
 공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어진다.
 
4 4
1 2 1
1 3 2
2 3 2
3 4 1
1 3

 x -2 -2 -1
'''