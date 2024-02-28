import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

nums=[]
while True:
    try:
        num=int(input())
        nums.append(num)
    except:
        break

def rec(array):
    #print(array)
    if len(array)==0:
        return

    if len(array)==1:
        print(array[0])
        return

    root=array[0]
    leftArray=[]
    rightArray=[]

    for i in range(1,len(array)):
        num=array[i]
        if num<root:
            leftArray.append(num)
        else:
            rightArray.append(num)

    rec(leftArray)
    rec(rightArray)
    print(root)
rec(nums)