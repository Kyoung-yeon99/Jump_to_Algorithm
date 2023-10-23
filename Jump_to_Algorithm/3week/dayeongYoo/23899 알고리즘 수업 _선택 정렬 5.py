n = int(input())
# 배열 a
a = list(map(int, input().split()))
# 배열 b
b = list(map(int, input().split()))


for i in range(n):
    max_idx = i #  가장 작은 값 저장
    for j in range(n-1, 0, -1):
        # 가장 작은 값이 다음 인덱스보다 클 때
        if a[max_idx] < a[j]:
            max_idx=j # 값 변경
    # 두 요소 변경
    a[i], a[max_idx]=a[max_idx], a[i]

    if a == b:
        print(1)

print(0)
