# 길이 m 인 수열 모두 구하기 => 완탐
# 1부터 n까지 중복 없이 m개 고르기 => 사용 기록 체크

n,m=map(int,input().split())
check = [False] * (n+1)

arr=[]
def recur(depth):
    if depth==m:
        print(*arr)
        return
    else:
        for i in range(1,n+1):
            if not check[i]:
                check[i]=True
                arr.append(i)
                recur(depth+1)
                check[i]=False
                arr.pop()

recur(0)