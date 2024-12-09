from sys import stdin
N = int(stdin.readline().rstrip())
arr = list(map(int,stdin.readline().rstrip().split()))

feature = 20000000000
answer_left, answer_right = 0, N-1
left = 0
right = N-1

while left < right:
    diff = arr[left] + arr[right]
    if diff == 0:
        answer_left, answer_right = arr[left], arr[right]
        break
    elif diff > 0: #0보다 크면
        if abs(feature) > abs(diff): #0보다 가까우면 값 업데이트
            feature = diff
            answer_left, answer_right = arr[left], arr[right]

        right -= 1 #오른쪽 한칸 당기기

    elif diff < 0: #0보다 작으면
        if abs(feature) > abs(diff): #0보다 가까우면 값 업데이트
            feature = diff
            answer_left, answer_right =  arr[left], arr[right]

        left += 1 #왼쪽 한칸 당기기

print(answer_left, answer_right)


