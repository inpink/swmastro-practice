import sys
input=sys.stdin.readline
import math

n,m=map(int,input().split())
booksInput=list(map(int,input().split()))
booksInput.sort()
minusBooks=[]
plusBooks=[]
for i in range(n):
    book=booksInput[i]
    if book<0:
        minusBooks.append(book)
    else:
        plusBooks.append(book)
#print(minusBooks,plusBooks)

if len(minusBooks)==0:
    minusBooks=[0]
if len(plusBooks)==0:
    plusBooks=[0]
maxAbs=max(abs(min(minusBooks)),max(plusBooks))
#print(maxAbs)
maxCount=1

minusBundleCount=math.ceil(len(minusBooks)/m)
plusBundleCount=math.ceil(len(plusBooks)/m)
#print(minusBundleCount,plusBundleCount)

ans=0
# minus 계산
for i in range(minusBundleCount):
    start=i*m
    if maxCount==1 and abs(minusBooks[start])==maxAbs:
        maxCount=0
        ans+=abs(minusBooks[start])
    else:
        ans+=abs(minusBooks[start])*2
    #print(ans)

# plus 계산
plusBooks.sort(reverse=True)
for i in range(plusBundleCount):
    start=i*m
    if maxCount==1 and abs(plusBooks[start])==maxAbs:
        maxCount=0
        ans+=abs(plusBooks[start])
    else:
        ans+=abs(plusBooks[start])*2
print(ans)
'''
그리디

음수와 양수는 함께 들고가는걸 계산할 필요가 없다 
어차피 2a+2b니까 따로보기


음수+양수 절대값이 가장 큰 숫자가 돌아오지 않고 끝나는 지점이 됨
2a 2b에서 a>b면 a+2b가 항상 2a+b보다 작으니까

음수/양수 나눠서 절대값 큰수대로 m개만큼 묶음
전체에서 가장 큰 수 제외하고 묶음의 절대값 가장 큰 수 *2 
 

'''