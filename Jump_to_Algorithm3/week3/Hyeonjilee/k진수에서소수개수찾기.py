def isprime(n):
    if n<2: return False
    i=2
    while i<=n**0.5:
        if n%i==0: return False
        i+=1
    return True
  
def solution(n, k):
    #n진수 변환하고
    #앞에서부터 훑으면서 소수 패턴 찾기
    num,i = 0,0
    num_list = ''
    while n>0: #진수변환
        div = n%k
        n //=k
        i+=1
        num_list+=str(div)
    num_list = num_list[-1::-1] #뒤집어야 함
    prime_list = num_list.split('0') 
    answer = 0
    for n in prime_list: 
        if n=='':continue
        if isprime(int(n)): #소수검사
            answer+=1
    return answer
