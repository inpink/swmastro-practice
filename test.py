print(1)

print(round(3.145,2)) # 3.15
print(round(4.145,2)) # 4.14
print(round(3.15,1)) # 3.1
print(round(4.15,1)) # 4.2
print(round(3.5)) # 4
print(round(4.5)) # 4
print(round(35,-1)) #40
print(round(45,-1)) #40

class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

head = Node(0)
nextNode = Node(1)
head.next=nextNode
print(head)


print("a".isupper())


n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
print(primes)


import re

text = "example@gmail.com"

# match() 예시
if re.match(r".+@gmail\.com", text):
    print("It matches with match()")

# findall() 예시
emails = "person1@test.com, person2@gmail.com, person3@yahoo.com"
all_emails = re.findall(r"[\w\.-]+@[\w\.-]+", emails)
print("All emails:", all_emails)



print(re.match("[a.b]","aa.bb"))
print(re.findall("[a.b]","aa.bb"))

print(re.match(r"(01)+","0101011"))
print(re.match(r"^[ㄱ-ㅎ가-힣]+$","안녕"))
print(re.match(r"^[ㄱ-ㅎ가-힣]+$","안녕1"))
print(re.match(r"[ㄱ-ㅎ가-힣]+","안녕1"))
print(re.match(r"[ㄱ-ㅎ가-힣]+","안녕1안녕"))
print(re.findall(r"[ㄱ-ㅎ가-힣]+","안녕1안녕"))
print(re.match(r"^[ㄱ-ㅎ가-힣]+$","안녕1"))
print(re.findall(r"(100+1+|01)+","10011001")) #이상함
print(re.match(r"(100+1+|01)+","10011001")) #이상함
print(re.findall(r"^(100+1+|01)+$","10011001"))  #OK
print(re.match(r"^(100+1+|01)+$","10011001"))  #OK
print(re.findall(r"^(100+1+|01)+$","1001100101"))  #OK
print(re.findall(r"(100+1+|01)+","10010111")) #이상함

print(re.match(r"^[\w\.-]+@[\w]+\.[a-zA-Z]+$","ab.-2@gmail.com"))
print(re.match(r"^[\w\.-]+@[\w]+\.[a-zA-Z]+$","ab.-2@gmail.com@"))

dic={1:2,3:4}
print(dic.values())
print(dic.items())
print(sorted(dic.keys()))

print(re.split(r"[+-]","55-50+40"))
print(re.findall(r"[+-]","55-50+40"))
print(sum([]))

a=[1,2,3,4,5]
print(a[:4])

from collections import deque

a=deque([1,2,3])
b=deque(a)
b.popleft()
print(a,b)

b.reverse()
print(b)
print("".join(deque(["1","2"])))