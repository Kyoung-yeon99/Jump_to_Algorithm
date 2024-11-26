import sys
N=int(sys.stdin.readline().rstrip())
arr=[]
answer = []
for _ in range(N):
    arr.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    count = 1
    for j in range(N):
        #몸무게 arr[i][0], 키 arr[i][1] 모두 크면 count + 1
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            count+=1
    answer.append(count)
print(*answer)
