'''
1. 일단 정렬한다.
2. 인덱스가 2 정도 차이나는 놈과 차이 값을 계산한다.
3. 그 중에서 최댓값이 정답.
'''

t = int(input())

for i in range(t):
    ans = 0
    leng = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for j in range(2, leng):
        ans = max(ans, arr[j] - arr[j - 2])
    print(ans)