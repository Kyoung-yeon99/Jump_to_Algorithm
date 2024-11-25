import sys
N=int(sys.stdin.readline().rstrip())
arr=[]

for _ in range(N):
    arr.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

def 덩치(arr):
    for i in range(N):
        count = 1
        for j in range(N):
            if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
                count+=1
        print(count, end=' ')

덩치(arr)

