n=int(input())

start=n//5
possible=False
while True:
    if start==-1:
        break

    if (n-(5*start))%3==0:
        possible=True
        break
    start-=1

if not possible:
    print(-1)
else:
    print(start+(n-(5*start))//3)