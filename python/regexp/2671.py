import sys
input = sys.stdin.readline

import re
s=input().rstrip()

if re.fullmatch(r"(100+1+|01)+",s):
    print("SUBMARINE")
else:
    print("NOISE")