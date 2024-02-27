import sys
input= sys.stdin.readline

import re

n=int(input())
for i in range(n):
    s1=input().rstrip()
    s2=input().rstrip()

    #1. 대소문자 맞추기
    s1=s1.lower()
    s2=s2.lower()

    #2. 공백 2개 이상은 1개로 맞춰주기
    s1=re.sub(r"\s{2,}"," ",s1)
    s2=re.sub(r"\s{2,}"," ",s2)

    #3. 문자열의 맨 앞 혹은 맨 뒤에 나타나는 공백 제거
    s1=s1.strip()
    s2=s2.strip()

    #5. 여는 괄호끼리는 종류를 구별하지 않는다.
    s1=re.sub(r"[\(\[\{]","(",s1)
    s2=re.sub(r"[\(\[\{]","(",s2)

    #6. 닫는 괄호끼리는 종류를 구별하지 않는다.
    s1=re.sub(r"[\)\]\}]",")",s1)
    s2=re.sub(r"[\)\]\}]",")",s2)

    #7. 쉼표(",")와 세미콜론(";")은 구별하지 않는다.
    s1=re.sub(r";",",",s1)
    s2=re.sub(r";",",",s2)

    #4. 특수 부호의 바로 앞이나 바로 뒤에 나오는 공백도 있으나 없으나 상관없다.
    notSpecific1=re.sub(r"\s*[().,:]+\s*","",s1)
    specific1=re.findall(r"[().,:]",s1)
    notSpecific2=re.sub(r"\s*[().,:]+\s*","",s2)
    specific2=re.findall(r"[().,:]",s2)
    print()
    '''print(notSpecific1)
    print(specific1)
    print(notSpecific2)
    print(specific2)

    print(s1)
    print(s2)'''

    if notSpecific1==notSpecific2 and specific1==specific2:
        ans="equal"
    else:
        ans="not equal"
    print("Data Set "+str(i+1)+": "+ans)

