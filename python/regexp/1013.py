import sys
input=sys.stdin.readline

import re

n=int(input())

for i in range(n):
    text=input().rstrip()
    if re.match("^(100+1+|01)+$",text):
        print("YES")
    else:
        print("NO")