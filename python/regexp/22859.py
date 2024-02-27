import sys
input= sys.stdin.readline

import re
print((1,2,3))
print(re.sub(r"\s*"," ","programmer"))
print(re.findall(r'a=(.*?),b=(.*?),c=(.*?),','kka=123,b=123,c=123,d=123'))
s=input().rstrip()
removeMain = re.findall(r'<main>(.*)</main>', s)[0] #1. main 제거
divs = re.findall(r'<div title="(.*?)">(.*?)</div>', removeMain) #. div-ps 쌍 만들기
# ?를 통해서 최소 일치 부분을 찾아줘야 모든 div를 찾을 수 있다!!!
#print(removeMain)
print(divs)

for title,ps in divs:
    print("title : "+title)
    notPureps=re.findall(r'<p>(.*?)</p>',ps)
    print(notPureps)
    for notPure in notPureps:
        removeTag = re.sub(r"<.*?>","",notPure) #태그에 일치하는 부분을 ""로 바꿔준다. 중요한 점, 여기서도 ?로 최소 일치 부분을 쓸 것!!
        removeSpace = re.sub(r"\s+"," ",removeTag) #\s*를 하면 모든 문자 뒤에 " "이 붙는다!!
        print(removeSpace)
