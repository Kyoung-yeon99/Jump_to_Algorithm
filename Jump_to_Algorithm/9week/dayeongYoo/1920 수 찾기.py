# n개의 숫자배열에서 m개의 숫자배열 속 숫자 여부 출력
# 이분탐색의 정석

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()  # 이분 탐색을 위해 오름차순 정렬


def bi_search(arr, tar, st, ed):
    while st <= ed:  # 시작점이 끝점보다 작거나 같을때까지만
        mid = (st + ed) // 2  # 중간점

        if arr[mid] == tar:  # 중간점이 찾으려는 데이터라면
            return 1
        elif arr[mid] > tar:  # 중간점이 찾으려는 데이터보다 크다면
            ed = mid - 1  # 끝점은 중간점 앞으로
        else:
            st = mid + 1
    return 0


for i in b:
    ans = bi_search(a, i, 0, n - 1)
    print(ans)
