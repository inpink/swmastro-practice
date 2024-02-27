import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    n=int(input())
    scores=[]
    for j in range(n):
        a,b=map(int,input().split())
        scores.append((a,b))
    scores.sort()
    #print(scores)
    ans=1
    topA,topB=scores[0]
    for j in range(1,n):
        thisA,thisB=scores[j]
        if topA>thisA or topB>thisB:
            ans+=1
            topA,topB=scores[j]
    print(ans)
'''
신규 사원 채용
 1차 서류심사와 2차 면접시험
 최고의 인재들만을 사원으로 선발하고 싶어 한다
 
 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다
 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
  이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램
  
  두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다
  
  지문이 좀 이상해

'''