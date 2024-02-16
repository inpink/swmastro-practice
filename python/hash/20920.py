import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic=dict()
for i in range(n):
    word = input().rstrip()
    if word in dic:
        dic[word]+=1
    else:
        dic[word]=1

#print(dic)
names=list(dic.keys())
names.sort(key=lambda x:(-dic[x],-len(x),x))
#print(names)
cut= list(filter(lambda x:(len(x)>=m), names))
#print(cut)

for i in cut:
    print(i)

'''
 단어의 개수 N(1~100000)
  단어의 길이 기준 M (1~10)
  알파벳 소문자로만 주어지며 
  
  에 길이가 $M$이상인 단어들만 외운다
  
  우선순위를 차례로 적용
  1,자주 나오는 단어일수록 앞에 배치한다.
  2.  단어의 길이가 길수록 앞에 배치
  3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치
'''