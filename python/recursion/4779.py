
def rec(standard,start,end,line):
    #print(standard,start,end,"".join(line))
    if standard==0:
        return
    rec(standard//3,start,start+standard-1,line)
    for i in range(start+standard,start+standard*2):
        line[i]=" "
    rec(standard//3,start+standard*2,end,line)

while True:
    try:
        n=int(input())
        line=["-" for i in range(3**n)]
        rec(3**n//3,0,3**n-1,line)
        print("".join(line))
    except EOFError:
        break