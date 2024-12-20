N = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

for id in range(N):
    left = 0
    right = N-1

    while left < right:
        if id == left:
            left+=1
            continue
        if id == right:
            right-=1
            continue

        s = arr[left] + arr[right]
        if s == arr[id]:
            # print(f'총계 {arr[id]} {arr[left]} + {arr[right]}, id : {left}, {right}')
            answer+=1
            break
        elif s > arr[id]: #오른쪽 당기기
                right -=1
        else: #sum이 적으면 왼쪽 당기기
            left += 1

print(answer)
