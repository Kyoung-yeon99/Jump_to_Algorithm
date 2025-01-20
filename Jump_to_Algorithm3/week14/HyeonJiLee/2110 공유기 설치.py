#이분탐색 - 인접한 두 공유기 사이의 최대 거리 -> 찾고자 하는 이진탐색 값 -> 공유기 수 = C
from sys import stdin

N, C = map(int, stdin.readline().rstrip().split())
arr = []
for _ in range(N):
    arr.append(int(stdin.readline().rstrip()))

#정렬하기
arr.sort()

def bin_search(arr, C, start, end):

    if start > end:
        return end

    mid = (start + end) // 2
    cnt = 1 #공유기 수
    last = arr[0] #마지막으로 탐색한 집 위치

    for h in arr:
        if h - last >= mid: #다음 집과의 거리가 mid 보다 크면
            cnt+=1 #공유기 설치하기
            last = h #마지막으로 탐색한 집 위치 업뎃
            if cnt == C: #공유기 개수 C개면 break
                break

    if cnt >= C:
        return bin_search(arr, C, mid+1, end)
    else:
        return bin_search(arr, C, start, mid -1)

print(bin_search(arr, C, 1, arr[-1] - arr[0]))