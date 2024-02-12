# 길이 m인 수열 모두 구하기 -> 완탐
# 1부터 n까지 중복없이 m개 -> check 배열
# 오름차순

n,m=map(int,input().split())
check = [False] *(n+1)

arr=[]

def recur(depth, start):
    if depth==m:
        print(*arr)
        return

    else:
        for i in range(start, n+1):
            if not check[i]:
                arr.append(i)
                check[i]=True
                recur(depth+1, i+1)
                arr.pop()
                check[i]=False

recur(0,1)