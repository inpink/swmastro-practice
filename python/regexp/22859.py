import sys
input= sys.stdin.readline

import re
s=input().rstrip()
splitedByP=s.split("<p>")
for i in splitedByP:
    print("i:",i)
    print("test search:",re.search(r'<div title=.*">',i))
    divs=re.findall(r'<div title=.*">',i)
    for j in divs:
        print("j:",j)
        print(re.search(r'".*"',j))
