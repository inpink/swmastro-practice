import sys
input=sys.stdin.readline

import re

n=int(input())
numbers=[]
for i in range(n):
    text=input().rstrip()
    finds=re.findall(r"[0-9]*",text)
    #print(finds)

    for find in finds:
        if find.isdigit():
            numbers.append(int(find))

numbers.sort()
for number in numbers:
    print(number)

