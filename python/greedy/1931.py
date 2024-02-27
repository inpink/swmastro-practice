import sys
input=sys.stdin.readline

n=int(input())
times=[]
for i in range(n):
    start,end=map(int,input().split())
    times.append((start,end))

times.sort()
#print(times)

x,y=times[0] # 0 6
count=1
for i in range(1,len(times)): # 이런 부분에서 확실히 range로 빼고가자
    start,end=times[i]
    if x<start and y>end:
        x=start
        y=end

    elif y<=start:
       count+=1
       x=start
       y=end
print(count)