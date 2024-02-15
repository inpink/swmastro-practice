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