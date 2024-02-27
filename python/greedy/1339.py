import sys
input=sys.stdin.readline
import heapq

n=int(input())
alphas=[]
positions=[[0,i] for i in range(ord('Z')+1)]
nums=[-1 for i in range(ord('Z')+1)]
for i in range(n):
    s=input().rstrip()
    alphas.append(s)
    size=len(s)
    for j in range(size):
        positions[ord(s[j])][0]-=10**(size-1-j)

heapq.heapify(positions)
#print(positions[ord('A'):])

top=9
while True:
    posNum,ordNum=heapq.heappop(positions)
    if posNum==0:
        break
    ##print(posNum,ordNum)
    nums[ordNum]=top
    top-=1
#print(nums[ord('A'):])

ans=0
for alpha in alphas:
    num=""
    for a in alpha:
        num+=str(nums[ord(a)])
    ans+=int(num)
    #print(num)
print(ans)
'''
단어 수학 문제를 푸는 숙제
단어 수학 문제는 N개의 단어로 이루어져 있으며,
 각 단어는 알파벳 대문자로만 이루어져 있다 (최대 길이 8)
 
 , 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제
  같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.
  N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성

단어의 개수 N(1 ≤ N ≤ 10)
'''