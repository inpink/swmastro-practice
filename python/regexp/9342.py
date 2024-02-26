import sys
input= sys.stdin.readline

import re
t=int(input())
for i in range(t):
    s=input().rstrip()
    if re.match(r"^[ABCDEF]{0,1}A+F+C+[ABCDEF]{0,1}$",s):
        print("Infected!")
    else:
        print("Good")
'''
염색체가 특정한 패턴인지를 확인
염색체는 알파벳 대문자 (A, B, C, ..., Z)로만 이루어진 문자열

 다음과 같은 규칙을 만족하는지 검사
- 문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
- 그 다음에는 A가 하나 또는 그 이상 있어야 한다.
- 그 다음에는 F가 하나 또는 그 이상 있어야 한다.
- 그 다음에는 C가 하나 또는 그 이상 있어야 한다.
- 그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.

r"^[ABCDEF]{0,1}A+F+C+[ABCDEF]{0,1}$"
'''