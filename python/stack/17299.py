import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))
dic=dict()
for num in nums:
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1
#print(dic)

ansList=['' for i in range(n)]
stack=[]
for i in range(n-1,-1,-1):
    num=nums[i]
    if len(stack)==0:
        ansList[i]=-1
        stack.append((num,dic[num])) #num,count
    else:
        while True:
            if len(stack)==0:
                break
            if stack[-1][1]<=dic[num]:
                stack.pop()
            else:
                break
        stack.append((num,dic[num]))
        if len(stack)>1:
            ansList[i]=stack[-2][0]
        else:
            ansList[i]=-1
    #print(i,num,stack,ansList)

print(*ansList)

'''
 오등큰수 NGF(i)를 구하려고 한다.
 Ai가 수열 A에서 등장한 횟수를 F(Ai)
 Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수
 그러한 수가 없는 경우에 오등큰수는 -1
 
앞에서부터 순회는 절대 안됨. 앞에서는 뒤의 시점을 알수없기때문에 절대 X
뒤에서부터 순회
1개인 경우 넣지 않음
스택에 자기보다 작거나 같은 값은 다 지우면서 대체 가능함 

'''