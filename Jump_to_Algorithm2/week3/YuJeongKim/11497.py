t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    arr.sort()

    _max=0

    # 두 통나무 간 높이 차의 최대값이 난이도
    # 인덱스 차가 2면 원소가 최대 높이 차
    for i in range(n-2):
        m=abs(arr[i]-arr[i+2])
        _max=max(m, _max)


    print(_max)